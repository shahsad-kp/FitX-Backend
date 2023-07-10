from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
    music = models.FileField(upload_to='category_audios/')

    def __str__(self):
        return f"Category {self.name}"


class CompletedCategory(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='completed_categories')
    user = models.ForeignKey(to='Users.User', on_delete=models.CASCADE, related_name='completed_categories')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} completed {self.category} on {self.date}"
