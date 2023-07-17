from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True)
    gender = models.CharField(choices=GENDERS, max_length=30, null=True)
    date_of_birth = models.DateField(verbose_name='Date of Birth', null=True)
    liked_categories = models.ManyToManyField(to='Category.Category', related_name='likes')
    is_trainer = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    first_name = None
    last_name = None

    def __str__(self):
        return f'@{self.username}'


class BurnedCalorie(models.Model):
    date = models.DateField(auto_now=True)
    calories = models.IntegerField()
    user_data = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='burned_calories')

    def __str__(self):
        return f'{self.user_data} burned {self.calories} calories at {self.date}'


class Weight(models.Model):
    date = models.DateField(auto_now=True)
    weight = models.FloatField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='weights')

    def __str__(self):
        return f'{self.user} weight is {self.weight} at {self.date}'


class Height(models.Model):
    date = models.DateField(auto_now=True)
    height = models.FloatField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='heights')

    def __str__(self):
        return f'{self.user} height is {self.height} at {self.date}'

