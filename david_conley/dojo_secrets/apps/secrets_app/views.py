from django.shortcuts import render, redirect, reverse
from django.db.models import Count
from ..dojo_secrets.models import User
from .models import Secret

def index(request):
    current_user = User.objects.currentUser(request)
    secrets = Secret.objects.annotate(num_likes=Count('liked_by'))

    context = {
        'user': current_user,
        'secrets': secrets,
    }
    # dont forget to pass the dictionary to the render method!
    return render(request, 'secretsapp/index.html', context)

def create(request):
    print "Inside the dreate method."
    if request.method == "POST":
        if len(request.POST['content']) != 0:
            current_user = User.objects.currentUser(request)
            secret = Secret.objects.createSecret(request.POST, current_user)

            print secret
    return redirect(reverse('secrets_app'))

def like(request, id):
    current_user = User.objects.currentUser(request)
    secret = Secret.objects.get(id=id)

    current_user.likes.add(secret)
    return redirect(reverse('secrets_app'))

def unlike(request, id):
    current_user = User.objects.currentUser(request)
    secret = Secret.objects.get(id=id)

    current_user.likes.remove(secret)
    return redirect(reverse('secrets_app'))


def delete(request, id):
    if request.method == "POST":
        secret = Secret.objects.get(id=id)
        current_user = User.objects.currentUser(request)

        if current_user.id == secret.user.id:
            secret.delete()

    return redirect(reverse('secrets_app'))
