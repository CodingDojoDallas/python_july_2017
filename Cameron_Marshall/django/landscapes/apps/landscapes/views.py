from django.shortcuts import render, HttpResponse, redirect
import random


# Create your views here.
def index(request):
	return render(request, 'landscapes/index.html')

def picture(request, number):
    end_paths = ['snow.jpg', 'desert.jpg', 'forest.jpg', 'vineyard.jpg', 'tropical.jpg']
    context = {}
    image_path = 'landscapes/img/'
    number = int(number)
    #check if number is out of range
    if number < 1 or number > 50:
        context['message'] = "Please keep your url in the range 1-50"
        number = random.randint(0,4)
        image_path += end_paths[number]
    
    #or, add to the image_path string but do not render until the end
    elif number >= 1 and number <=10:
        image_path += end_paths[0]

    elif number >= 11 and number <=20:
        image_path += end_paths[1]

    elif number >= 21 and number <=30:
        image_path += end_paths[2]

    elif number >= 31 and number <=40:
        image_path += end_paths[3]

    elif number >= 41 and number <=50:
        image_path += end_paths[4]

    context['image_path'] = image_path
    return render(request, 'landscapes/picture.html', context)