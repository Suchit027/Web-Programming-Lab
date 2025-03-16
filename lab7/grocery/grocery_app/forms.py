from django import forms
choices = [('wheat', True), ('jaggery', True), ('dal', True)]
class GroceryForm(forms.Form):
    wheat = forms.BooleanField(widget= forms.CheckboxInput, required= False)
    jaggery = forms.BooleanField(widget= forms.CheckboxInput, required= False)
    dal = forms.BooleanField(widget= forms.CheckboxInput, required= False)
    