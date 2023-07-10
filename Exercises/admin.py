from django.contrib import admin

from Exercises.models import Exercise, CompletedExercise

admin.site.register(Exercise)
admin.site.register(CompletedExercise)
