from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    file = forms.FileField()

class UploadLicenseForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()