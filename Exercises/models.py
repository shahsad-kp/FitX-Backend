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

    def __str__(self):
        return f"Exercise {self.name}"


class CompletedExercise(models.Model):
    exercise = models.ForeignKey(to=Exercise, on_delete=models.CASCADE, related_name='completed_exercises')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='completed_exercises')
    user = models.ForeignKey(to='Users.User', on_delete=models.CASCADE, related_name='completed_exercises')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} completed {self.exercise} of {self.category} on {self.date}"
