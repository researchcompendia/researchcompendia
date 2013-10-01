import base64
import datetime
import hmac
import sha

from dateutil.tz import tzlocal
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .forms import CompanionForm
from .models import CompanionArticle


def companion(request):
    if request.method == 'POST':
        form = CompanionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = CompanionForm()
    return render(request, 'create.html', {'form': form})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def s3signature(request):
    """ Return a signature so that files can be uploaded to the s3 materials bucket """

    if 'filename' not in request.QUERY_PARAMS:
        return Response({"message": "missing filename from request"}, status=status.HTTP_400_BAD_REQUEST)
    if 'article_id' not in request.QUERY_PARAMS:
        return Response({"message": "missing article_id from request"}, status=status.HTTP_400_BAD_REQUEST)

    key_id = settings.AWS_MATERIALS_UPLOADER_KEY_ID
    resource = "/{bucket}/{username}/{article_id}/{filename}".format(
        bucket=settings.AWS_MATERIALS_BUCKET,
        username=request.user.username,
        article_id=request.QUERY_PARAMS['article_id'],
        filename=request.QUERY_PARAMS['filename'],
    )

    # Canonical strings and key signing are documented in the s3 developer guide.
    # http://s3.amazonaws.com/doc/s3-developer-guide/RESTAuthentication.html
    amz_date = datetime.datetime.now(tzlocal()).strftime('%a, %d %b %Y %H:%M:%S %Z')
    canonical_string = "POST\n\n\nx-amz-date:{}\n{}".format(amz_date, resource)
    h = hmac.new(settings.AWS_MATERIALS_UPLOADER_SECRET, canonical_string, sha)
    signature = base64.encodestring(h.digest()).strip()

    return Response({
        'signature': signature,
        'bucket_resource': resource,
        'key_id': key_id,
        'x-amz-date': amz_date,
        'canonical_string': canonical_string,
        'Authorization': 'AWS {}:{}'.format(key_id, signature),
    })


class CompanionArticleListView(generic.ListView):
    model = CompanionArticle
    template_name = 'supportingmaterials/index.html'
    context_object_name = 'companion_article_list'


class CompanionArticleDetailView(generic.DetailView):
    model = CompanionArticle
    template_name = 'supportingmaterials/detail.html'
