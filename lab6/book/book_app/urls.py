from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover, name='cover'),
    path('meta/', views.meta, name='meta'),
    path('review/', views.review, name='review'),
    path('pubinfo/', views.pubinfo, name='pubinfo')
]