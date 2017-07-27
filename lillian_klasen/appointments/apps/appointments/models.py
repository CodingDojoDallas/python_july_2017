from __future__ import unicode_literals

from django.db import models

class AppointmentManager(models.Manager):
    def validateDate(self, form_data):
        errors = []

        if len(form_data['date']) == 0:
            errors.append("Date is required")

        if len(form_data['time']) == 0:
            errors.append("Time is required")

        return errors


class Appointment(models.Model):
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AppointmentManager()
