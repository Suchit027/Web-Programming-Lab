from django.shortcuts import render, redirect
from .models import Person, Room
# Create your views here.


def index(request):
    ob = Room.objects.all()
    return render(request, 'roomapp/index.html', {'rooms': ob})

def book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        room = request.POST.get('room')
        rooms = Room.objects.filter(name = room)
        room = None
        for x in rooms:
            room = x
        room.allocated = 1
        room.save()
        ob = Person()
        ob.name = name
        ob.email = email
        ob.room = room
        ob.save()
        return redirect('roomapp/index.html')
    return render(request, 'roomapp/book.html', {'rooms': Room.objects.all()})