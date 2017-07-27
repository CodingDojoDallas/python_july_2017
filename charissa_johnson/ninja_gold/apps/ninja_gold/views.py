from django.shortcuts import render, HttpResponse, redirect
import random, datetime
# Create your views here.
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
		addGold = random.randrange(-50,50)
		request.session['money'] += addGold

	time = datetime.datetime.now().time()
	timestamp = time.strftime("%I:%M:%S")

	note = "Earned {} gold from the {}! {}".format(request.session['money'], buildingtype, timestamp)

	request.session['activity'].insert(0, note)
		
	return redirect('/')

def reset(request):
	if 'reset' not in request.session:
		request.session['money'] = 0
		request.session.pop('activity')

	return redirect('/')