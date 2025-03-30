from django.shortcuts import render, redirect
from .models import Works, Lives
from .forms import WorkForm, LiveForm
# Create your views here.

def index(request):
    return render(request, 'employeeapp/index.html')

def add_works(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WorkForm()
    return render(request, 'employeeapp/add_works.html', {'form': form})

def find(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        ob = Works.objects.filter(company = company)
        ret = []
        for work in ob:
            person = Lives.objects.filter(name= work)
            for p in person:
                ret.append({'name': work.name, 'city': p.city})
        return render(request, 'employeeapp/find.html', {'ans': ret})
    return render(request, 'employeeapp/find.html', dict())
