from django.shortcuts import render, redirect
import random, string

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
import random
import string
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    context = {
        'count' : request.session['count']
    }
    return render(request, 'random_word/index.html', context)

def generate(request):
    request.session['count'] +=1
    request.session['random_word'] = ' '.join(random.choice(string.ascii_uppercase) for x in range(14)     )
    context2 = {
        'random_word' : request.session['random_word'],
        'count' : request.session['count']
    }
    return render(request, 'random_word/index.html', context2)
