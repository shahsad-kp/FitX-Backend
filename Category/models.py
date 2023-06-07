from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
    music = models.FileField(upload_to='category_audios/')

