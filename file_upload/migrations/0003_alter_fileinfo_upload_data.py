# Generated by Django 4.0.3 on 2022-03-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file_upload", "0002_alter_file_table_fileinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fileinfo",
            name="upload_data",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]