# Generated by Django 4.1.2 on 2022-11-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0010_doctorpatient_approved_filesharerequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
        migrations.AddField(
            model_name='file',
            name='comments',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='file',
            name='diagnosis',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='file',
            name='medication',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='file',
            name='symptoms',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='file',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='FileData',
        ),
    ]
