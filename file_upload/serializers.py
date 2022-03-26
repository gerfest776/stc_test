from rest_framework import serializers

from file_upload.models import File, FileInfo
from file_upload.service.get_filename import get_filename
from file_upload.service.get_size import convert_size


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("file",)

    def create(self, validated_data):
        """
        create file and file_info
        """
        current_file = File.objects.create(**validated_data).file
        FileInfo.objects.create(
            file=current_file.instance,
            name=get_filename(current_file.name),
            size=convert_size(current_file.size),
            type=current_file.name.split(".")[-1],
        )

        return current_file.instance

    def to_representation(self, instance):
        representation = {"id": instance.id}
        return representation
