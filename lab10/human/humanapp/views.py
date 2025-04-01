from django.shortcuts import render, redirect
from .forms import HumanForm
from .models import Human

def human_crud(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        
        if form.is_valid():
            human = form.cleaned_data['selected_human']
            
            if 'load' in request.POST:
                initial_data = {
                    'selected_human': human,
                    'first_name': human.first_name,
                    'last_name': human.last_name,
                    'phone': human.phone,
                    'address': human.address,
                    'city': human.city,
                }
                return render(request, 'humanapp/human_crud.html', {
                    'form': HumanForm(initial=initial_data)
                })
                
            elif 'update' in request.POST:
                human.first_name = form.cleaned_data['first_name']
                human.last_name = form.cleaned_data['last_name']
                human.phone = form.cleaned_data['phone']
                human.address = form.cleaned_data['address']
                human.city = form.cleaned_data['city']
                human.save()
                
            elif 'delete' in request.POST:
                human.delete()
                
            return redirect('humanapp/human_crud')
    
    return render(request, 'humanapp/human_crud.html', {'form': HumanForm()})
