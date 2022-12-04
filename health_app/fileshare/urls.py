from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myfiles/', views.myfiles, name='myfiles'),
    path('create_file/', views.create_file, name='create_file'),
    path('delete_file/<str:pk>/', views.delete_file, name='delete_file'),
    path('update_file/<str:pk>/', views.update_file, name='update_file'),
    path('add_doctor/<str:pk>', views.add_doctor, name='add_doctor'),
    path('download_file/<str:pk>/', views.download_file, name='download_file'),
    path('profile/', views.profile, name='profile'),
    path('delete_license/<str:pk>/', views.delete_license, name='delete_license'),
    path('all_doctors/', views.all_doctors, name='all_doctors'),
    path('request_doctor/<str:pk>/', views.request_doctor, name='request_doctor'),
    path('my_doctors/', views.my_doctors, name='my_doctors'),
    path('shared_files/', views.shared_files, name='shared_files'),
    path('patient_data/', views.patient_data, name='patient_data'),
    path('get_patient_requests/', views.get_patient_requests, name='get_patient_requests'),
    path('approve_patient/<str:pk>/', views.approve_patient, name='approve_patient'),
    path('deny_patient/<str:pk>/', views.deny_patient, name='deny_patient')
]