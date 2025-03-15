from django.shortcuts import render

# Create your views here.


def getinput(request):
    if request.method == 'POST':
        img = request.POST.get('img')
        bgcolor = request.POST.get('bgcolor')
        fsize = request.POST.get('fsize')
        color = request.POST.get('color')
        text = request.POST.get('msg')
        # note how is renders the request to another html file
        # note is uses the appName/htmlFile format
        return render(request, 'magazine_app/display.html', {'img': img, 'bgcolor': bgcolor, 'fsize': fsize,
                                                             'color': color, 'text': text})
    return render(request, 'magazine_app/input.html')

def display(request):
    pass
