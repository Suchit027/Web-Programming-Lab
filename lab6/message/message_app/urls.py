from django.urls import path
from . import views

urlpatterns = [
    path('', views.message, name= 'message')
]