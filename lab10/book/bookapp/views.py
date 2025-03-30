from django.shortcuts import render, redirect
from .models import Book, Author, Publisher
from .forms import BookForm, AuthorForm, PublisherForm
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'bookapp/index.html', {'books': books})

def add_books(request):
    if request.method == 'POST':
        form = Book(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Book()
    return render(request, 'bookapp/add_book.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = Author(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Author()
    return render(request, 'bookapp/add_book.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = Publisher(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Publisher()
    return render(request, 'bookapp/add_book.html', {'form': form})