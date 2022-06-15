from django.db import models

# Create your models here.
class stud(models.Model):
    sname=models.CharField(max_length=50)
    semail=models.CharField(max_length=50)
    saddress=models.CharField(max_length=50)
    smobile=models.IntegerField()
    sgender=models.CharField(max_length=1)