from django.db import models

from Category.models import Category


class Exercise(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    demo = models.FileField(upload_to='exercise_demos/')
    count = models.PositiveIntegerField(blank=True)
    duration = models.DurationField(blank=True)
    category = models.ManyToManyField(to=Category, related_name='exercises')
