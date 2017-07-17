from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

# Create your views here.
def index(request):
	if not 'activity' in request.session:
		request.session['gold'] = 0
		request.session['activity'] = []
	return render(request, 'ninja_gold/index.html')


def process_money(request, money_method):
    
    if request.method == "POST":
        if money_method == "farm":
            gold_gained = random.randint(10,20)
            request.session['gold'] += gold_gained
            request.session['activity'].insert(0, "Earned " + str(gold_gained) + " gold from the farm! " + str(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")))
        elif money_method == "cave":
            gold_gained = random.randint(5,10)
            request.session['gold'] += gold_gained
            request.session['activity'].insert(0, "Earned " + str(gold_gained) + " gold from the cave! " + str(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")))
        elif money_method == "house":
            gold_gained = random.randint(2,5)
            request.session['gold'] += gold_gained
            request.session['activity'].insert(0, "Earned " + str(gold_gained) + " gold from the cave! " + str(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")))
        elif money_method == "casino":
            gold_gained = random.randint(-50,50)
            request.session['gold'] += gold_gained
            if gold_gained >= 0:
                request.session['activity'].insert(0, "Earned " + str(gold_gained) + " gold from the casino! " + str(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")))
            else:
                request.session['activity'].insert(0, "Lost " + str(gold_gained) + " gold from the casino " + str(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")))
        else:
            request.session['activity'].insert(0, "Invalid route")
            pass

        
        #code here
        return redirect('index')
    else:
        return redirect('index')

def reset(request):
    request.session.clear()
    return redirect('index')