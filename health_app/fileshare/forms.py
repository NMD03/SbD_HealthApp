from django import forms
from django.forms import ModelForm
from .models import *


class FileForm(ModelForm):

    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=300, required=False)
    file = forms.FileField(required=True)

    class Meta:
        model = File
        fields = ('name', 'description', 'file')


class UploadLicenseForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


DOCTOR_CHOICES = []
class AddDoctorForm(forms.Form):
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