from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    mob = models.CharField(max_length=10)