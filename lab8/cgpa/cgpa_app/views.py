from django.shortcuts import render
from .forms import CGPAForms
# Create your views here.

def create(request):
    if request.method == 'POST':
        form = CGPAForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            marks = form.cleaned_data['marks'] / 50
            return render(request, 'cgpa_app/display.html', {'name': name, 'marks': marks})
    else:
        form = CGPAForms()
    return render(request, 'cgpa_app/input.html', {'form': form})
