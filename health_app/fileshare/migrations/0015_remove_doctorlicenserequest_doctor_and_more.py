# Generated by Django 4.1.2 on 2022-12-02 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fileshare', '0014_alter_file_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorlicenserequest',
            name='doctor',
        ),
        migrations.AddField(
            model_name='doctorlicenserequest',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
