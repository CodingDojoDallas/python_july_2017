from django.shortcuts import render, redirect

def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 1

    return render(request, "survey/index.html")

def process(request):
    if request.method == "POST":
        request.session['counter'] = request.session['counter'] + 1
        
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
        return render(request, 'survey/result.html')
