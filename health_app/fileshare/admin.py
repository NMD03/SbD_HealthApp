from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(DoctorPatient)
admin.site.register(File)
#admin.site.register(FileShare)
#admin.site.register(FileShareRequest)
#admin.site.register(FileData)
admin.site.register(DoctorFile)
admin.site.register(DoctorLicense)

