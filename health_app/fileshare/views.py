from django.shortcuts import redirect, render

from .decorators import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


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
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = File(file=request.FILES['file'], patient=request.user.patient, name=request.POST['title'], description=request.POST['description'])
            instance.save()
            return redirect('myfiles')
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
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = File(file=request.FILES['file'], patient=request.user.patient, name=request.POST['title'], description=request.POST['description'])
            instance.save()
            return redirect('myfiles')
    context = {'form': form}
    return render(request, 'fileshare/create_file.html', context)

def download_file(request, pk):
    file = File.objects.get(id=pk)
    ## todo: download file
    return render(request, 'fileshare/download.html', {'file': file})

def add_doctor(request, pk):
    file = File.objects.get(id=pk)
    if request.method == 'POST':
        ### add doctor to file

        return redirect('myfiles')
    return render(request, 'fileshare/add_doctor.html', {'file': file})

def profile(request):
    user = request.user
    try:
        license = user.doctor.doctorlicense_set.all()
    except:
        license = None
    form = UploadLicenseForm()
    if request.method == 'POST':
        form = UploadLicenseForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                doctor = user.doctor
            except:
                Doctor.objects.create(
                    user=user,
                )
                group = Group.objects.get(name='doctor')
                user.groups.add(group)
            instance = DoctorLicense(doctor=user.doctor, license=request.FILES['file'], title=request.POST['title'])
            instance.save()
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
    # für alle doctors die user finden

    print(doctors)
    context = {"doctors": doctors}
    return render(request, 'fileshare/all_doctors.html', context)

def request_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == 'POST':
        ### send request to doctor

        return redirect('all_doctors')
    return render(request, 'fileshare/request_doctor.html', {'doctor': doctor})