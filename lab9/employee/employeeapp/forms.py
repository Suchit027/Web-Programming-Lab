from django import forms
from .models import Works, Lives

class WorkForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['name', 'company', 'salary']

class LiveForm(forms.ModelForm):
    class Meta:
        model = Lives
        fields = ['name', 'street', 'city']
