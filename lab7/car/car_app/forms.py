from django import forms

manufacturers = [('toyota', 'toyota'), ('honda', 'honda'), ('ford', 'ford')]

class CarForm(forms.Form):
    manufacturer = forms.ChoiceField(choices=manufacturers)
    model_name = forms.CharField(max_length=100)
    