from django.shortcuts import render, HttpResponse, redirect
import random, string

def index(request):
        if not 'attempt' in request.session:
            request.session['attempt'] = 1

        if request.session['attempt'] > 0:
            word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

            word = {
            'word': word
            }

        return render(request, 'random_generator/index.html', word)

def generate(request):
    if request.method == 'POST':
        request.session['attempt'] = request.session['attempt'] + 1

        return redirect('/')
