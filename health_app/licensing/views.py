from django.shortcuts import redirect, render
from fileshare.models import *
from django.contrib.auth.models import Group
from django.http import FileResponse
from encrypted_files.base import EncryptedFile

# Create your views here.

def get_doctor_requests(request):
    license_requests = DoctorLicense.objects.filter(approved=False)
    context = {'license_requests': license_requests}
    return render(request, 'licensing/get_doctor_requests.html', context)

def approve_license(request, pk):
    license = DoctorLicense.objects.get(id=pk)
    page ='approve_license'
    user = license.doctor.user
    if request.method == 'POST':
        license.approved = True
        license.save()
        try:
            doctor = user.doctor
        except:
            Doctor.objects.create(
                user=user,
            )
            group = Group.objects.get(name='doctor')
            user.groups.add(group)
        return redirect('get_doctor_requests')
    context = {'item': license, 'page': page}
    return render(request, 'licensing/approve_license.html', context)

def deny_license(request, pk):
    license = DoctorLicense.objects.get(id=pk)
    page ='deny_license'
    if request.method == 'POST':
        license.delete()
        return redirect('get_doctor_requests')
    context = {'item': license, 'page': page}
    return render(request, 'licensing/deny_license.html', context)

def download_license(request, pk):
    license = DoctorLicense.objects.get(id=pk)
    data = license.license
    return FileResponse(EncryptedFile(data), as_attachment=True, filename=license.title + '.' + license.license.name.split('.')[-1])

