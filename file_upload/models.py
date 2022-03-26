from django.db import models


class File(models.Model):
    file = models.FileField(null=False)

    class Meta:
        db_table = "file"


class FileInfo(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    upload_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "file_info"
