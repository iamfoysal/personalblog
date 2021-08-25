from django.db import models
from django.utils import timezone


# Create your models here.
class post(models.model):
    title =  models.CharField(max_length=100)
    content = models.
