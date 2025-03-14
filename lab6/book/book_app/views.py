from django.shortcuts import render

# Create your views here.
def cover(request):
    return render(request, 'book_app/cover.html')

def meta(request):
    return render(request, 'book_app/meta.html')

def review(request):
    return render(request, 'book_app/review.html')

def pubinfo(request):
    return render(request, 'book_app/pubinfo.html')