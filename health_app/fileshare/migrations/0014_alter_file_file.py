# Generated by Django 4.1.2 on 2022-12-01 15:39

from django.db import migrations, models
import fileshare.models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0013_remove_file_comments_remove_file_diagnosis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=fileshare.models.upload_location),
        ),
    ]