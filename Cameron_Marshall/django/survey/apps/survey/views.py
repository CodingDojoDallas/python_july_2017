from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, 'survey/index.html')

def result(request):
    return render(request, 'survey/result.html')

#handles form on index page
def handle_survey(request):
    print request.method
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['count'] += 1
        return redirect('/result')
    else:
        return redirect('/')