from django.shortcuts import render, redirect, HttpResponse
import random
VALUES = ['Item One', 'Item Two', 'Item Three', 'Item Four', 'Item Five', 'Item Six', 'Item Seven', 'Item Eight', 'Item Nine', 'Item Ten']
# Create your views here.
def index(request):
    return render(request, 'surprise/index.html')

def results(request):
    context = {}
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        random.shuffle(VALUES)
        context['numbers'] = VALUES[:amount]
    elif request.method == 'GET':
        context['message'] = "Please use our form to reach this page :)"

    return render(request, 'surprise/results.html', context)