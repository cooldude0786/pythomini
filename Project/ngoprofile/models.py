from django.db import models

# Create your models here.


class Ngo_Details(models.Model):
    ngoname = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)
    vision = models.CharField(max_length=255)
    founderstmt = models.CharField(max_length=255)
    startdate = models.DateField()
    operatonal = models.CharField(max_length=255)
    fromstate = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)

def __str__(self):
    return self.ngoname
