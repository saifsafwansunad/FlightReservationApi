import email
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Flight (models.Model):
    filghtNumber=models.CharField(max_length=20,unique=True)
    operatingAirlines=models.CharField(max_length=20)
    departureCity=models.CharField(max_length=20)
    arrivalCity=models.CharField(max_length=20)
    dateofDeparture=models.DateField()
    estimatedTimeofDeparture=models.TimeField()


class Passenger(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    middleName=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=20)



class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)


