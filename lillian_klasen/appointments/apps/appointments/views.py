from django.shortcuts import render, redirect
from .models import Appointment
from django.contrib import messages
import datetime

def index(request):
    return render(request, 'appointments/index.html')

def success(request):
    if 'appointment_id' in request.session:
        appointment_id = request.session['appointment_id']

        appointment = Appointment.objects.get(id=appointment_id)

        context = {
            'appointment': appointment
            }

    return render(request, 'appointments/success.html', context)

def schedule(request):
    if request.method == 'POST':
        errors = Appointment.objects.validateDate(request.POST)

        appointments = Appointment.objects.all()
        date_try = request.POST['date']

        if not errors:
            for appointment in appointments:
                if Appointment.objects.filter(date__contains=date_try):
                    errors.append("That time is not available")

                # appointment = Appointment.objects.create(
                #     date = request.POST['date'],
                #     time = request.POST['time']
                # )

                if appointment:

                    request.session['appointment_id'] = appointment.id

                return redirect('/success')

        else:
            if errors:
                for error in errors:
                    messages.error(request, error)

        return redirect('/')


def logout(request):
    if 'appointment_id' in request.session:
        request.session.pop('appointment_id')
        return redirect('/')
