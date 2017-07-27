from django.shortcuts import render
import random

VALUES = [
'charissa',
'lillian',
'banana',
'flaming',
'adios amigos',
'coding dojo',
'ninjas',
'weird'
]

def index(request):
    return render(request, 'surprise_me/index.html')

def results(request):
    if request.method == 'POST':
        request.session['number'] = request.POST['number']

    random.shuffle(VALUES)

    list = []

    for item in range(0, int(request.POST['number'])):
        list.append(VALUES[item])

    request.session['list'] = list

    return render(request, 'surprise_me/results.html')
