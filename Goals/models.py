from django.db import models


class WeeklyCalorieGoal(models.Model):
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE, related_name='weekly_calorie_goals')
    week = models.DateField()
    goal = models.IntegerField()

    def __str__(self):
        return f'Calorie goal for {self.user} in {self.week} week'

    class Meta:
        ordering = ['-week']


class WeeklyCategoryGoal(models.Model):
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE, related_name='weekly_category_goals')
    week = models.DateField()
    goal = models.IntegerField()

    def __str__(self):
        return f'Category goal for {self.user} in {self.week} week'

    class Meta:
        ordering = ['-week']


class WeeklyExerciseGoal(models.Model):
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE, related_name='weekly_exercise_goals')
    week = models.DateField()
    goal = models.IntegerField()

    def __str__(self):
        return f'Exercise goal for {self.user} in {self.week} week'

    class Meta:
        ordering = ['-week']
