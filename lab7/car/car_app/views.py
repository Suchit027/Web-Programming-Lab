from django.shortcuts import render
from .forms import CarForm
# Create your views here.

def create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            manufacturer = form.cleaned_data['manufacturer']
            model_name = form.cleaned_data['model_name']
            return render(request, 'car_app/display.html', {'manufacturer': manufacturer, 'model_name': model_name})
    else:
        form = CarForm()
    return render(request, 'car_app/input.html', {'form': form})

def display(request):
    pass