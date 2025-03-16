from django import forms


class StudentForm(forms.Form):
    name = forms.CharField()
    roll_no = forms.CharField()
    choices = [('Maths', 'maths'), ('Physics', 'physics'),
               ('Chemistry', 'chemistry')]
    subjects = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=choices)
