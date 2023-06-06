from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
    music = models.FileField(upload_to='category_audios/')


class Exercise(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    demo = models.FileField(upload_to='exercise_demos/')
    count = models.PositiveIntegerField(blank=True)
    duration = models.DurationField(blank=True)
    category = models.ManyToManyField(to=Category, related_name='exercises')
