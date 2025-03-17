from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput, required= True)
    password = forms.CharField(widget= forms.TextInput, required= False)
    email = forms.EmailField(widget= forms.EmailInput, required= False)
    contact_no = forms.IntegerField(widget= forms.NumberInput, required= False)
    