from django.db import models

from Category.models import Category


class Exercise(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    demo = models.FileField(upload_to='exercise_demos/')
    count = models.PositiveIntegerField(null=True)
    duration = models.DurationField(null=True)
    video_link = models.CharField(max_length=250, blank=True)
    burn_calorie = models.IntegerField()
    focused_area = models.CharField(null=True, max_length=250)
    category = models.ManyToManyField(to=Category, related_name='exercises')
