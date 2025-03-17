from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def create(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            contact_no = form.cleaned_data['contact_no']
            return render(request, 'register_app/success.html', {'username': username, 'email': email, 'contact_no': contact_no})
    else:
        form = RegisterForm()
        return render(request, 'register_app/register.html', {'form': form})