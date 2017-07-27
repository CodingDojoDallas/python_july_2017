from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    return render(request, 'landscape/index.html')

def all(request):
    return HttpResponse('<img src="../static/landscape/images/snow.jpg">')

def show(request, landscape):

    if (landscape <= '10'):
        return HttpResponse('<img src="../static/landscape/images/snow.jpg">')

    if (landscape <= '10'):
        return HttpResponse('<img src="../static/landscape/images/snow.jpg">')

    if (landscape > '10' and landscape <= '20'):
        return HttpResponse('<img src="../static/landscape/images/desert.jpg">')

    if (landscape > '20' and landscape <= '30'):
        return HttpResponse('<img src="../static/landscape/images/forest.jpg">')

    if (landscape > '30' and landscape <= '40'):
        return HttpResponse('<img src="../static/landscape/images/vineyard.jpg">')

    if (landscape > '40' and landscape <= '50'):
        return HttpResponse('<img src="../static/landscape/images/tropical.jpg">')

    else:
        return HttpResponse('<img src="../static/landscape/images/ocean.jpg">')
