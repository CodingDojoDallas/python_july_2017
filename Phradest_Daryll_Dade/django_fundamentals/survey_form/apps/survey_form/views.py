from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    if 'count' not in request.session:
       request.session['count'] = 1
    return render(request, 'survey_form/index.html')

def result(request):

    return render(request, 'survey_form/result.html')

#def submit(request):


#    return render(request, 'survey_form/result.html', contex)

def process(request):

        request.session['name'] = request.POST['name'],
    	request.session['location'] = request.POST['location'],
    	request.session['language'] = request.POST['language'],
    	request.session['comments'] = request.POST['comments']

    #context = {'count1' : request.session['count'],
    #'your_name1' : request.post['name'],
    #'dojo_locations1' : request.post['location'],
    #'language1' : request.post['language'],
    #'comment1' : request.post['comment']
    #}

    #return render(request, 'survey_form/result.html', contex)
        return redirect('result')
