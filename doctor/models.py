from django.db import models

class Doctor(models.Model):
    #first_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    #email = models.EmailField()
    #phone_number = models.CharField(max_length=15)
 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
