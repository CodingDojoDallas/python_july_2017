from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.

def random_word():
    random_string = get_random_string(length=10)
    return random_string
    
def index(request):    
    if not 'count' in request.session:
        request.session['count'] = 1
    if request.session['count'] > 0:
        randomWord = {
            "word": random_word()
        }
    else:
        randomWord = {
            "word": "Don't push the generate button"
        }
    return render(request, 'first_app/index.html', randomWord)

def generate(request):
    if request.method == "POST":
        request.session['count'] += 1
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    if request.method == "POST":
        request.session['count'] = 0
        return redirect('/')
    else:
        return redirect('/')