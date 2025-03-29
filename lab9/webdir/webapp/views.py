from django.shortcuts import render, redirect
from .models import Category, Page
from .forms import CategoryForm, PageForm
# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'webapp/index.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'webapp/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PageForm()
    return render(request, 'webapp/add_page.html', {'form': form})