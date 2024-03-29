from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.BooleanField(default=False)
    fees = models.IntegerField()

    def __str__(self):
        return self.first_name

class Login(models.Model):
    username = models.CharField(max_length=30)
    passwd = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username       