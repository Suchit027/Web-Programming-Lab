from django import forms
from .models import Person, Room

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'room']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['price', 'bhk', 'name', 'allocated']