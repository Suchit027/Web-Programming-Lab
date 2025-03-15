from django.shortcuts import render

# Create your views here.
def calculate(request):
    if request.method == 'POST':
        op = request.POST.get('op')
        # note that input is always a string; convert it to int
        n1 = int(request.POST.get('n1'))
        n2 = int(request.POST.get('n2'))
        if op == 'add':
            return render(request, 'calculate.html', {'ans': str(n1 + n2)})
        elif op == 'sub':
            return render(request, 'calculate.html', {'ans': str(n1 - n2)})
        elif op == 'mul':
            return render(request, 'calculate.html', {'ans': str(n1 * n2)})
        elif op == 'div':
            if n2 == 0:
                return render(request, 'calculate.html', {'ans': 'error'})
            return render(request, 'calculate.html', {'ans': str(n1 / n2)})
        else:
            return render(request, 'calculate.html', {'ans': 'error'})
    return render(request, 'calculate.html', dict())
