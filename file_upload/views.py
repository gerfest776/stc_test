import os

from django.http import Http404, HttpResponse
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from file_upload.models import File, FileInfo
from file_upload.pagination import DynamicPageNumberPagination
from file_upload.serializers import FileInfoSerializer, FileSerializer


class FileViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = DynamicPageNumberPagination

    def get_queryset(self):
        if self.action == "info":
            return FileInfo.objects.all()
        if self.action == "download":
            return File.objects.filter(id=self.kwargs["pk"]).first()
        else:
            return self.queryset

    def get_serializer_class(self):
        if self.action == "info":
            return FileInfoSerializer
        else:
            return self.serializer_class

    @action(methods=["get"], detail=False, url_name="file_info")
    def info(self, request):
        return self.list(request)

    @action(methods=["get"], detail=True, url_name="file_download")
    def download(self, request, pk):
        obj = self.get_queryset()
        if obj:
            filename = obj.file.path
            with open(filename, "rb") as fh:
                response = HttpResponse(
                    fh.read(), content_type="application/vnd.ms-excel"
                )
                response[
                    "Content-Disposition"
                ] = "inline; filename=" + os.path.basename(filename)
                return response
        raise Http404
