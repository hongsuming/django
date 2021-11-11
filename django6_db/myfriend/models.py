from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=14)
    age = models.IntegerField()
    address = models.CharField(max_length=50)