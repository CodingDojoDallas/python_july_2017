from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    date = datetime.datetime.now().date()
    dateF = date.strftime('%b %d, %Y')
    time = datetime.datetime.now().time()
    timeF = time.strftime('%I:%M:%S')

    date_time = {
    "date": dateF,
    "time": timeF
    }
    return render(request, 'time_display/index.html', date_time)
