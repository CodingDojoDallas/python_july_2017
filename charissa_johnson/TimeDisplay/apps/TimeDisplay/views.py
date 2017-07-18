from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
	print ("*")*100
	date = datetime.datetime.now().date()
	date_str = date.strftime("%b %d, %Y")
	time = datetime.datetime.now().time()
	time_str = time.strftime("%I:%M:%S")

	print date_str

	date_dict = {
		"date": date_str,
		"time": time_str
	}

	return render(request, 'TimeDisplay/index.html', date_dict)