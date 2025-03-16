from django.shortcuts import render
from .forms import GroceryForm
from django.http import HttpRequest

def create(request):
    if not request.session.get('selected_items'):
        request.session['selected_items'] = {'wheat': False, 'jaggery': False, 'dal': False}
    
    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            wheat = form.cleaned_data['wheat']
            jaggery = form.cleaned_data['jaggery']
            dal = form.cleaned_data['dal']
            
            # Update session with selected items
            request.session['selected_items']['wheat'] = wheat
            request.session['selected_items']['jaggery'] = jaggery
            request.session['selected_items']['dal'] = dal
            
            # Save session changes
            request.session.modified = True
            
            # Render template with updated session data
            context = {
                'wheat': request.session['selected_items']['wheat'],
                'jaggery': request.session['selected_items']['jaggery'],
                'dal': request.session['selected_items']['dal'],
                'form': GroceryForm()
            }
            return render(request, 'grocery_app/display.html', context)
    else:
        form = GroceryForm()
        context = {
            'wheat': request.session.get('selected_items', {}).get('wheat', False),
            'jaggery': request.session.get('selected_items', {}).get('jaggery', False),
            'dal': request.session.get('selected_items', {}).get('dal', False),
            'form': form
        }
    return render(request, 'grocery_app/display.html', context)
