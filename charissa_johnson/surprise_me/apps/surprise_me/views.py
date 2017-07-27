from django.shortcuts import render, HttpResponse, redirect
import random 
VALUES = [
	'lillian',
	'charissa',
	'tashi',
	'ruby',
	'banana',
	'apple',
	'pizza',
	'turtle'
]
# Create your views here.
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

		context = {
			'list': list
		}
		
	return render(request, 'surprise_me/results.html', context)