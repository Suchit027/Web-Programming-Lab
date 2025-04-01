from django import forms
from .models import Human

class HumanForm(forms.Form):
    selected_human = forms.ModelChoiceField(
        queryset=Human.objects.all(),
        label="Select Human",
        empty_label="Choose a person"
    )
    first_name = forms.CharField(required= False)
    last_name = forms.CharField(required= False)
    phone = forms.CharField(required= False)
    address = forms.CharField(required= False)
    city = forms.CharField(required= False)
