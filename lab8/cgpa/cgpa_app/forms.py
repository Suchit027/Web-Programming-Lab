from django import forms

class CGPAForms(forms.Form):
    # note widget forms.TextInput, forms.NumberInput
    name = forms.CharField(widget= forms.TextInput)
    marks = forms.IntegerField(widget= forms.NumberInput)
    