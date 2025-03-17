from django.shortcuts import render

# Create your views here.
count = 0

def create(request):
    global count
    if count == 0:
        del request.session['votes']
        count += 1
    if not request.session.get('votes'):
        request.session['votes'] = {'good': 0, 'satisfactory': 0, 'bad': 0}
    if request.method == 'POST':
        tag = request.POST.get('review')
        request.session['votes'][tag] += 1
        request.session.modified = True
        summ = sum(request.session['votes'].values())
        return render(request, 'book_app/display.html', {'good': str((request.session['votes']['good'] / summ) * 100) + '%',
                                                         'satisfactory': str((request.session['votes']['satisfactory'] / summ) * 100) + '%' ,
                                                         'bad': str((request.session['votes']['bad'] / summ) * 100) + '%'})
    else:
        return render(request, 'book_app/display.html', {'good': '', 'satisfactory': '', 'bad': ''})