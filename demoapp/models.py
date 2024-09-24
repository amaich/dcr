from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.BooleanField()


