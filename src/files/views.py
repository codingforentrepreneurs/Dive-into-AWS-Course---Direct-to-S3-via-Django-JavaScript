from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
# Create your views here.

from .models import S3File

class DownloadView(View):
    def get(self, request, id, *args, **kwargs):
        file_obj = get_object_or_404(S3File, id=id)
        if request.user != file_obj.user:
            raise Http404
        url  = file_obj.get_download_url()
        return HttpResponseRedirect(url)