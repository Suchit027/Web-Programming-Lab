from django.shortcuts import render
from datetime import date

# Create your views here.
def elligible(request):
    if request.method == 'POST':
        empid = request.POST.get('emp')
        doj = int(request.POST.get('doj')[: 4])
        # note how date is used
        now = int(date.today().year)
        if now - doj > 5:
            return render(request, 'elligibility.html', {'promotion': 'yes'})
        else:
            return render(request, 'elligibility.html', {'promotion': 'no'})
    else:
        return render(request, 'elligibility.html', dict())
