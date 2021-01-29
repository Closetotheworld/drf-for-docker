from django.db import models

# Create your models here.

class Routine(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    author = models.CharField(max_length=30)