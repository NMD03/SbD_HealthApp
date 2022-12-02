from django.http import FileResponse
from django.shortcuts import redirect, render
from encrypted_files.base import EncryptedFile
from .decorators import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.conf import settings

import reportlab


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'fileshare/index.html')

@login_required(login_url='login')
@patient_only
def myfiles(request):
    files = request.user.patient.file_set.all()
    context = {"files": files}
    return render(request, 'fileshare/myfiles.html', context)

@login_required(login_url='login')
@patient_only
def create_file(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            extension = request.FILES['file'].name.split('.')[-1]
            if extension in settings.ALLOWED_EXTENSIONS and request.FILES['file'].size < settings.MAX_FILE_SIZE:
                instance = File(patient=request.user.patient, name=request.POST['name'], file=request.FILES['file'])
                instance.save()
                messages.success(request, 'File uploaded successfully')
                return redirect('myfiles')
            else:
                messages.error(request, 'File type or size not allowed')
                return redirect('create_file')
    context = {'form': form}
    return render(request, 'fileshare/create_file.html', context)

@login_required(login_url='login')
@patient_only
def delete_file(request, pk):
    file = File.objects.get(id=pk)
    page = 'delete_file'
    if request.method == 'POST':
        file.delete()
        return redirect('myfiles')
    context = {'item': file, 'page': page}
    return render(request, 'fileshare/delete.html', context)

@login_required(login_url='login')
@patient_only
def update_file(request, pk):
    file = File.objects.get(id=pk)
    form = FileForm(instance=file)
    if request.method == 'POST':
        form = FileForm(request.POST, instance=file)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('myfiles')
    context = {'form': form}
    return render(request, 'fileshare/create_file.html', context)


def download_file(request, pk):
    file = File.objects.get(id=pk)
    data = file.file
    return FileResponse(EncryptedFile(data), as_attachment=True, filename=file.name + '.' + file.file.name.split('.')[-1])


def profile(request):
    user = request.user
    # try:
    #     license = user.doctor.doctorlicense_set.all()
    #     print('license')
    # except:
    #     license = None

    license = DoctorLicense.objects.filter(doctor=user.patient, approved=True)
        
    form = UploadLicenseForm()
    if request.method == 'POST':
        form = UploadLicenseForm(request.POST, request.FILES)
        if form.is_valid():
            extension = request.FILES.get('file', None).name.split('.')[-1]
            if extension in settings.ALLOWED_EXTENSIONS and request.FILES['file'].size < settings.MAX_FILE_SIZE:
                # try:
                #     doctor = user.doctor
                # except:
                #     Doctor.objects.create(
                #         user=user,
                #     )
                    # group = Group.objects.get(name='doctor')
                    # user.groups.add(group)
                try:
                    instance = DoctorLicense(doctor=user.patient, license=request.FILES['file'], title=request.POST['title'], approved=False)
                    instance.save()
                    messages.success(request, 'Request sent successfully')
                except:
                    messages.error(request, 'Already sent request')
                return redirect('profile')
            else:
                messages.error(request, 'File type or size not allowed')
                return redirect('profile')
    context = {"user": user, "license": license, "form": form}
    return render(request, 'fileshare/profile.html', context)

def delete_license(request, pk):
    license = DoctorLicense.objects.get(id=pk)
    page = 'delete_license'
    user = request.user
    if request.method == 'POST':
        license.delete()
        if len(user.doctor.doctorlicense_set.all()) < 1:
            user.doctor.delete()
            group = Group.objects.get(name='doctor')
            user.groups.remove(group)
        return redirect('profile')
    context = {'item': license, 'page': page}
    return render(request, 'fileshare/delete.html', context)

def all_doctors(request):
    doctors = Doctor.objects.all()
    context = {"doctors": doctors}
    return render(request, 'fileshare/all_doctors.html', context)

def request_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    form = RequestDoctorForm()
    if request.method == 'POST':
        form = RequestDoctorForm(request.POST)
        ### send request to doctor
        if form.is_valid():
            instance = DoctorPatient(doctor=doctor, patient=request.user.patient)
            instance.save()
            return redirect('all_doctors')
    context = {"form": form, "doctor": doctor}
    return render(request, 'fileshare/request_doctor.html', context)

def my_doctors(request):
    doctor_patient = request.user.patient.doctorpatient_set.all()
    doctors = []
    for doctor in doctor_patient:
        doctors.append(doctor.doctor)
    context = {"doctors": doctors}
    return render(request, 'fileshare/my_doctors.html', context)

def shared_files(request):
    files = File.objects.filter(patient=request.user.patient, shared=True)
    print(files)
    context = {"files": files}
    return render(request, 'fileshare/shared_files.html', context)

def add_doctor(request, pk):
    file = File.objects.get(id=pk)
    form = AddDoctorForm(request=request)
    if request.method == 'POST':
        ### add doctor to file
        form = AddDoctorForm(request.POST, request=request)
        if form.is_valid():
            instance = DoctorFile(file=file, doctor=Doctor.objects.get(id=form.cleaned_data['doctor']))
            instance.save()
            file.shared = True
            file.save()
            return redirect('shared_files')
        return redirect('myfiles')
    context = {"form": form, "file": file}
    return render(request, 'fileshare/add_doctor.html', context)

def patient_data(request):
    files = DoctorFile.objects.filter(doctor=request.user.doctor)
    context = {"files": files}
    return render(request, 'fileshare/patient_data.html', context)
