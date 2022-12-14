from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return f"files/{instance.patient.user.username}/{instance.name}.{filename.split('.')[-1]}"

def license_upload_location(instance, filename):
    return f"licenses/{instance.doctor.user.username}/{instance.title}.{filename.split('.')[-1]}"
    

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class DoctorPatient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.doctor.user.username + ' - ' + self.patient.user.username

class File(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default="")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_location, null=True, blank=True)
    shared = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class FileShareRequest(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.file.name


class DoctorFile(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.file.name

class DoctorLicense(models.Model):
    doctor = models.OneToOneField(Patient, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    license = models.FileField(upload_to=license_upload_location)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.doctor.user.username + ' - ' + self.title
