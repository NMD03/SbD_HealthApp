# Generated by Django 4.1.2 on 2022-10-29 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.user')),
            ],
        ),
        migrations.CreateModel(
            name='FileShareRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.doctor')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.file')),
            ],
        ),
        migrations.CreateModel(
            name='FileShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('doctor_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.doctorpatient')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.file')),
            ],
        ),
        migrations.CreateModel(
            name='FileData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.BinaryField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.file')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.patient'),
        ),
        migrations.AddField(
            model_name='doctorpatient',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.patient'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileshare.user'),
        ),
    ]
