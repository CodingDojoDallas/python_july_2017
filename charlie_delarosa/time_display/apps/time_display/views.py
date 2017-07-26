from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    date_time = datetime.now()
    #theDateTime = str(datetime.now())
    theTime = str(date_time.time())
    theDate = str(date_time.date())

    context = {
    #"current_date" : str(datetime.date())
        "current_date" : theDate,
        "current_time" : theTime,
    }
    return render(request, 'index.html', context)
