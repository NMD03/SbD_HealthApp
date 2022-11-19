from django import forms
from .models import *

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    file = forms.FileField()

class UploadLicenseForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

DOCTOR_CHOICES = []
# doctors = Doctor.objects.all()
# for doctor in doctors:
#     DOCTOR_CHOICES.append((doctor.id, doctor.user.first_name + ' ' + doctor.user.last_name + ' email: ' + doctor.user.email))
class AddDoctorForm(forms.Form):
    #doctor = forms.CharField(label="Which Doctor want you to have acces to this file?", widget=forms.Select(choices))
    doctor = forms.ChoiceField()
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AddDoctorForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].choices = self.get_doctors()

    def get_doctors(self):
        doctor_patient = self.request.user.patient.doctorpatient_set.all()
        doctors = []
        for dp in doctor_patient:
            doctors.append(Doctor.objects.get(id=dp.doctor.id))
        for doctor in doctors:
            DOCTOR_CHOICES.append((doctor.id, doctor.user.first_name + ' ' + doctor.user.last_name + ' email: ' + doctor.user.email))
        return DOCTOR_CHOICES
    
class RequestDoctorForm(forms.Form):
    message = forms.CharField(max_length=300)