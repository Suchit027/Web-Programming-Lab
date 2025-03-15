from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover, name='cover'),
    # note that the name here will be used in the url used in the html files
    path('meta/', views.meta, name='meta'),
    path('review/', views.review, name='review'),
    path('pubinfo/', views.pubinfo, name='pubinfo')
]