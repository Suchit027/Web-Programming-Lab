from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'productapp/index.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'productapp/add_product.html', {'form': form})