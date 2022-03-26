from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from file_upload.models import File
from file_upload.serializers import FileSerializer


class FileViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
