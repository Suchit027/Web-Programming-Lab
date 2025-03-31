from django.shortcuts import render, redirect
from .models import Book, Author, Publisher
from .forms import BookForm, AuthorForm, PublisherForm
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'bookapp/index.html', {'books': books})

def add_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'bookapp/add_book.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'bookapp/add_book.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PublisherForm()
    return render(request, 'bookapp/add_book.html', {'form': form})