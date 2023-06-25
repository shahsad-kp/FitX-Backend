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
    first_name = None
    last_name = None


class BurnedCalorie(models.Model):
    date = models.DateField()
    calories = models.IntegerField()
    user_data = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='burned_calories')


class Weight(models.Model):
    date = models.DateField()
    weight = models.FloatField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='weights')


class Height(models.Model):
    date = models.DateField()
    height = models.FloatField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='heights')


class CompletedCategory(models.Model):
    date = models.DateField()
    category_id = models.ForeignKey(
        to='Category.Category',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='completed_categories')
