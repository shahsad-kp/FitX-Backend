from django.db import models

from Users.models import User


class TransformationImage(models.Model):
    user = models.ForeignKey(to=User, related_name='transformation_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='transformation/')
    date = models.DateField(auto_now=True)
