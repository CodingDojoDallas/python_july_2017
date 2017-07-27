from django.shortcuts import render

def index(request):
  return render(request, 'disappearing_ninjas/index.html')

def ninja(request):
    return render(request, 'disappearing_ninjas/ninja.html')

def blue(request):
  return render(request, 'disappearing_ninjas/blue.html')

def orange(request):
  return render(request, 'disappearing_ninjas/orange.html')

def red(request):
  return render(request, 'disappearing_ninjas/red.html')

def purple(request):
  return render(request, 'disappearing_ninjas/purple.html')
