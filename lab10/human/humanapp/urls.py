from django.urls import path
from . import views

urlpatterns = [
    path('human/', views.human_crud, name='human_crud'),
]
