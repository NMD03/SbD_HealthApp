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
]