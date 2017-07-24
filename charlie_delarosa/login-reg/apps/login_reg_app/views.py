from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    print "Inside the index method"
    return render(request, 'login_reg_app/index.html')

def success(request):
    print "Inside the success method."

    if 'user_id' in request.session:
        user_id = request.session['user_id']
        # current_user = User.objects.get(id=user_id)
        context = {
            'current_user': User.objects.get(id=user_id)
        }
        return render(request, 'login_reg_app/success.html', context)
    return redirect('/')

def logout(request):
    request.session.pop('user_id')
    return redirect('/')

def create(request):
    print "Inside the create method."

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.validate(form_data)
        if check:
            print check
            return redirect('/')

        #Valid form data
        user = User.objects.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = form_data['password']
        )
        request.session['user_id'] = user.id

        return redirect('/success')

    return redirect('/')

def login(request):
    print "Inside the login method."

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.login(form_data)
        #print type(check) == type(User())
        if type(check) == type(User()):
            request.session['user_id'] = check.id
            return redirect('/success')
        print check
    return redirect('/')
