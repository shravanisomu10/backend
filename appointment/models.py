from django.db import models
from django.utils import timezone 


class Appointment(models.Model):
   
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    doctors_name = models.CharField(max_length=255)
    #time = models.TimeField()
    date = models.DateTimeField(default=timezone.now)

