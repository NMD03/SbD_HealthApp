from django.db import models
from django.contrib.auth.models import User


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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.doctor.user.username + ' - ' + self.patient.user.username

class File(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class FileShare(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctor_patient = models.ForeignKey(DoctorPatient, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.file.name

class FileShareRequest(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.file.name

class FileData(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    data = models.BinaryField()
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
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    license = models.FileField(upload_to='licenses/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.doctor.user.username + ' - ' + self.title


# class FileShareRequestResponse(models.Model):
#     file_share_request = models.ForeignKey(FileShareRequest, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     response = models.BooleanField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.file_share_request.file.name

# class DoctorPatientFile(models.Model):
#     doctor_patient = models.ForeignKey(DoctorPatient, on_delete=models.CASCADE)
#     file = models.ForeignKey(File, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.doctor_patient.doctor.user.username + ' - ' + self.doctor_patient.patient.user.username + ' - ' + self.file.name
