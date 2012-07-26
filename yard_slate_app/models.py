from django.db import models

# Create your models here.
class YardSlate(models.Model):
    title = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    photo_one = models.ImageField(upload_to='./')
    photo_two = models.ImageField(upload_to='slate_images')
    photo_three = models.ImageField(upload_to='slate_images')
    photo_four = models.ImageField(upload_to='slate_images')