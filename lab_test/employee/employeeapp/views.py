from django.shortcuts import render
from .forms import EmpolyeeForm, FirstPageForm
from .models import Employee, FirstPage

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EmpolyeeForm(request.POST)
        if form.is_valid():
            