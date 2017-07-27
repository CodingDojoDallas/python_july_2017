from django.shortcuts import render, redirect
import random, datetime

def index(request):
    if 'money' not in request.session:
        request.session['money'] = 0

    if 'activity' not in request.session:
        request.session['activity'] = []

    money = request.session['money']
    activity = request.session['activity']

    ninja_dictionary = {
    'money': money,
    'activities': activity
    }

    return render(request, 'ninja_gold/index.html', ninja_dictionary)

def process_money(request):
    buildingtype = request.POST['building']

    if buildingtype == 'farm':
        addGold = random.randrange(10,21)
        request.session['money'] += addGold

    elif buildingtype == 'cave':
        addGold = random.randrange(5,11)
        request.session['money'] += addGold

    elif buildingtype == 'house':
        addGold = random.randrange(2,6)
        request.session['money'] += addGold

    elif buildingtype == 'casino':
        addGold = random.randrange(-50,51)
        request.session['money'] += addGold


    time = datetime.datetime.now().strftime('%I:%M:%S')
    timestamp = str(time)

    note = "Earned {} gold from the {}! {}".format(addGold, buildingtype, timestamp)

    print request.session['activity']

    request.session['activity'].insert(0, note)


    return redirect('/')

def reset(request):
    if 'reset' not in request.session:
        request.session['money'] = 0
        request.session.pop('activity')
    return redirect('/')
