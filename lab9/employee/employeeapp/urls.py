from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('add_works/', views.add_works, name='add_works'),
    path('find/', views.find, name= 'find')
]