from django.urls import path

from . import views

urlpatterns = [
    path('get_requests', views.get_doctor_requests, name='get_doctor_requests'),
    path('approve_license/<str:pk>/', views.approve_license, name='approve_license'),
    path('deny_license/<str:pk>/', views.deny_license, name='deny_license'),
    path('download_license/<str:pk>/', views.download_license, name='download_license'),
]