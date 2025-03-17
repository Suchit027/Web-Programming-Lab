from django import forms

class CGPAForms(forms.Form):
    name = forms.CharField(widget= forms.TextInput)
    marks = forms.IntegerField(widget= forms.NumberInput)
    