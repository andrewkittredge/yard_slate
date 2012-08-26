from django.db import models

# Create your models here.
class Slate(models.Model):
    title = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    
    photo_one = models.ImageField(upload_to='slate_images', blank=True)
    photo_two = models.ImageField(upload_to='slate_images', blank=True)
    photo_three = models.ImageField(upload_to='slate_images', blank=True)
    photo_four = models.ImageField(upload_to='slate_images', blank=True)