import base64
import datetime
import hmac
import logging
import sha

from django.conf import settings

from dateutil.tz import tzlocal
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from lib.storage import upload_path
from lib import crossref

logger = logging.getLogger(__name__)


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
