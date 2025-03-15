from django.shortcuts import render

# Create your views here.


def message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # note how checkboxes are handled
        # note that getlist is needed here
        style = request.POST.getlist('style')
        if not style:
            bold = italic = 'normal'
            underline = 'none'
        else:
            # note these if else
            if 'bold' in style:
                bold = 'bold'
            else:
                bold = 'normal'
            if 'italic' in style:
                italic = 'italic'
            else:
                italic = 'normal'
            if 'underline' in style:
                underline = 'underline'
            else:
                underline = 'none'
        color = request.POST.get('color')
        msg = request.POST.get('msg')
        return render(request, 'message_app/display.html', {'msg': msg, 'bold': bold, 'italic': italic, 'underline': underline, 'name': name, 'color': color})
    return render(request, 'message_app/display.html')
