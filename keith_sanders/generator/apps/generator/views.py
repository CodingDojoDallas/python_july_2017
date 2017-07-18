from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    
    request.session['count'] += 1

    unique_id = get_random_string(length=14)

    context = {
        'word': unique_id
    }

    return render(request, 'generator/index.html', context)








