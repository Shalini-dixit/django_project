from django.db import models
from django.db.models.base import Model

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    webpage = models.ForeignKey(Webpage)
    date =models.DateField()

    def __str__(self):
        return str(self.date)
