from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # note cleaned_data
            name = form.cleaned_data['name']
            roll_no = form.cleaned_data['roll_no']
            subs = form.cleaned_data['subjects']
            subjects = ','.join(subs)
            return render(request, 'student_app/display.html', {'name': name, 'roll_no': roll_no, 'subjects': subjects})
    else:
        form = StudentForm()
    return render(request, 'student_app/input.html', {'form': form})
