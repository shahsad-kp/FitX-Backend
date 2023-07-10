from django.contrib import admin

from Goals.models import WeeklyCalorieGoal, WeeklyCategoryGoal, WeeklyExerciseGoal

admin.site.register(WeeklyCalorieGoal)
admin.site.register(WeeklyCategoryGoal)
admin.site.register(WeeklyExerciseGoal)
