from django.shortcuts import render, HttpResponse
from time import strftime, localtime

# Create your views here.
def index(request):
    date_time = {
        'date': strftime('%b %d, %Y'),
        'time': strftime('%I:%M %p', localtime())
    }
    return render(request,'time_display/index.html', date_time)