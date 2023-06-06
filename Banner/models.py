from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='utilities/')
