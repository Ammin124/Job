from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.imgUpdate, name='imgUpload'),
    path('file/', views.fileUpdate, name='file'),
]
