from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "survey_form/index.html")

def process(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    
    request.session['count'] +=1


    return redirect('/result')

def result(request):

    request.session['ft_name'] = request.POST['name'],
    request.session['place'] = request.POST['location'],
    request.session['language'] = request.POST['language'],
    request.session['comment'] = request.POST['comment']
        
    name = request.session['ft_name'],
    location = request.session['place'],
    language = request.session['language'],
    comment = request.session['comment']

    context = {
        'name': name,
        'location': location,
        'language': language,
        'comment': comment
    }

    return render(request, 'survey_form/result.html', context)

    
