from django import forms
from .models import StudentCR, Choice

class StudentCRForm(forms.ModelForm):
    class Meta:
        model = StudentCR
        fields = ['name', 'section']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['cr', 'vote']
        