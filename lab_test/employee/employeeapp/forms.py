from django import forms
from .models import Employee, FirstPage

class EmpolyeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'date', 'salary', 'designation']