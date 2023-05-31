from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=3)
    email = models.EmailField()
    gender = models.CharField(max_length=30)