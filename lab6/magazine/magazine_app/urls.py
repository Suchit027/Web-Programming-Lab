from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.getinput, name='input')
]