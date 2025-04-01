from django.shortcuts import render
from .forms import StudentCRForm
from .models import StudentCR

# Create your views here.
def index(request):
    crs = StudentCR.objects.all()
    return render(request, 'studentapp/index.html', {'crs': crs})
