import base64
import datetime
import hmac
import json
import logging
import sha

from django.conf import settings
from django.core.files import File
from django.http import Http404

from dateutil.tz import tzlocal
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from compendia.models import Article, Verification
from lib.storage import upload_path
from lib import crossref, verify


logger = logging.getLogger('researchcompendia.api')


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def s3signatures(request):
    """ Returns a signature so that files can be uploaded to the s3 materials bucket """

    if 's3_object_name' not in request.QUERY_PARAMS:
        return Response({"message": "missing s3_object_name from request"}, status=status.HTTP_400_BAD_REQUEST)

    s3name = upload_path(request.user.username, request.QUERY_PARAMS['s3_object_name'])
    # Canonical strings and key signing are documented in the s3 developer guide.
    # http://s3.amazonaws.com/doc/s3-developer-guide/RESTAuthentication.html
    amz_date = datetime.datetime.now(tzlocal()).strftime('%a, %d %b %Y %H:%M:%S %Z')
    canonical_string = "POST\n\n\nx-amz-date:{}\n{}".format(amz_date, s3name)
    h = hmac.new(settings.AWS_SECRET_ACCESS_KEY, canonical_string, sha)
    signature = base64.encodestring(h.digest()).strip()

    return Response({
        'signed_request': signature,
        'url': s3name,
        'key_id': settings.AWS_ACCESS_KEY_ID,
        'x-amz-date': amz_date,
        'canonical_string': canonical_string,
        'Authorization': 'AWS {}:{}'.format(settings.AWS_ACCESS_KEY_ID, signature),
    })


class VerificationList(APIView):
    """
    List recent verification results for an compendia, or create a new verification
    """
    def get(self, request, pk):
        """ get recent verifications for a compendia
        """
        logging.debug('getting')
        article = self.get_object(pk)
        verifications = article.verification_set.all()[:5]
        # should be in compendia/serializers.py
        logging.debug(verifications)
        verify_list = []
        for v in verifications:
            verify_list.append({
                'id': v.id,
                'status': v.status,
                'stdout': v.stdout,
                'stderr': v.stderr,
                'requestid': v.requestid,
                'parameters': json.loads(v.parameters),
                'archive_info': json.loads(v.archive_info),
                'archive_file_url': v.archive_file.url,
                'created': v.created,
            })
        logging.debug(verify_list)
        return Response({'verifications': verify_list}, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """ Submits a request to run a compendia page, WARNING: UNSAFE

        Assumptions:

        The article exists. The article has an admin zipped code archive file that
        adheres to the convention. There is a main* in the zip file
        that dumps results to compendiaoutput/.

        Example reponses:

        {
        "message": "ok",
        "output_files": [{"file": "file1", "bytes": 1024, "size": "1K"}],
        "stderr": "",
        "stdout": ""
        }

        {"message": "nothing to run"}
        {"message": "used default parameters"}
        {"message": "Compendia does not exist"}

        curl -v -X POST "http://hostname/api/v1/verification/2/"

        """
        article = self.get_object(pk)

        # this is a stub.  For the purpose of a small demo, we will kick off
        # some jobs via curl to populate some results, and then leave the
        # website to get the existing results.
        if 'parameters' not in request.POST:
            logger.debug("using default parameters %s", request.POST)
            return Response({"message": "Request was made with default parameters. Fetched cached results."},
                status=status.HTTP_200_OK)

        request = {
            'id': 'messageidnotusedyet',
            'compendia_id': pk,
            'path_to_target': article.verification_archive_file.path,
        }
        try:
            results = verify.verify(request)
            save_verification(article, results)
            result_status = results.get('status', status.HTTP_201_CREATED)
            return Response(results, status=result_status)
        except:
            # I don't have any customized exceptions yet just do this for now. apologies!
            logger.exception("evil badness from verify request", exc_info=True)
            return Response({'message': 'We could not complete the verification request and' +
                ' the administrators have been notified'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_object(self, pk):
        try:
            article = Article.objects.get(pk=pk)
            return article
        except Article.DoesNotExist:
            raise Http404


# this doesn't belong here, I'll move it
def save_verification(article, results):
    stdout = results.get('stdout', '')
    stderr = results.get('stderr', '')
    requestid = results.get('requestid', '')
    output_files = results.get('output_files', [])

    verification = Verification(
        article=article,
        stdout=stdout,
        stderr=stderr,
        requestid=requestid,
        archive_info=json.dumps({'output_files': output_files}),
    )

    if 'path_to_zipped_output' in results:
        with open(results['path_to_zipped_output']) as fh:
            archive_file = File(fh)
            verification.archive_file.save('verification.zip', archive_file, save=False)

    verification.save(force_insert=True)


@api_view(['POST'])
def doi_crossref(request):
    """ Returns information based on crossref's doi query service

    request: The request is required to have a valid doi string. valid means TODO

    response: The response will contain a json dict of data with keys
    corresponding to attributes of the Article and Collaborator models. Any
    attributes we were unable to get from the crossref service will not be
    included in the dict.
    """

    if 'doi' not in request.POST:
        logger.debug("doi not in request %s", request.POST)
        return Response({"message": "missing DOI from request"}, status=status.HTTP_400_BAD_REQUEST)

    doi_data = crossref.query(settings.CROSSREF_PID, request.POST['doi'])
    return Response(doi_data)
