from audioop import maxpp
from django.db import models 

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=40)

    def __str__(self):
        return self.name