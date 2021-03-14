from os import name
from django.db import models
from django.db.models import fields

# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=255 , null=True)
    def __str__(self):
        return str(self.name)

class Country(models.Model):
    name  = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)

class Rate(models.Model):
    rate = models.IntegerField(null=True , blank=True)
    def __str__(self):
        return str(self.rate)

class Movie(models.Model):
    title      = models.CharField(max_length=255)
    overView   = models.TextField()
    year       = models.DateField()
    poster     = models.ImageField(upload_to="day1/posters")
    video      = models.FileField(upload_to="day1/video")
    categories = models.ManyToManyField(Category)
    country    = models.ForeignKey(Country , null=True , on_delete=models.SET_NULL)
    rate       = models.ForeignKey(Rate    , null=True , on_delete=models.SET_NULL)
    htmlID     = models.IntegerField(null=True , blank=True)
    # rate       = models.OneToOneField(Rate , null=True , on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.title)