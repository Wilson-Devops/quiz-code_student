from django.db import models


class student(models.Model):
    Name    =models.CharField(max_length=20)
    Email   =models.EmailField()
    phone   =models.CharField(max_length=10)
    Course  =models.CharField(max_length=20)
    Password=models.CharField(max_length=10)

def __str__(self):
        return self.Name

