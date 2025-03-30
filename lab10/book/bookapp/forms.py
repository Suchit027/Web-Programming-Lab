from django import forms
from .models import Book, Publisher, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'date', 'author', 'publisher']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'street', 'country', 'state', 'website']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['firstname', 'lastname', 'email']