from django.db import models


class WeeklyCalorieGoal(models.Model):
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE, related_name='weekly_calorie_goals')
    last_date = models.DateField()
    calorie_goal = models.IntegerField()

    def __str__(self):
        return f'{self.user} - {self.last_date} - {self.calorie_goal}'

    class Meta:
        ordering = ['-last_date']
        unique_together = ['user', 'last_date']


class WeeklyCategoryGoal(models.Model):
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE, related_name='weekly_category_goals')
    last_date = models.DateField()
    category_goal = models.IntegerField()

    def __str__(self):
        return f'{self.user} - {self.last_date} - {self.category_goal}'

    class Meta:
        ordering = ['-last_date']
        unique_together = ['user', 'last_date', 'category_goal']


class WeeklyExerciseGoal(models.Model):
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE, related_name='weekly_exercise_goals')
    last_date = models.DateField()
    exercise_goal = models.IntegerField()

    def __str__(self):
        return f'{self.user} - {self.last_date} - {self.exercise_goal}'

    class Meta:
        ordering = ['-last_date']
        unique_together = ['user', 'last_date', 'exercise_goal']
