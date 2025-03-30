from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_book/', views.add_books, name= 'add_book'),
    path('add_author/', views.add_author, name= 'add_author'),
    path('add_publisher/', views.add_publisher, name= 'add_publisher')
]