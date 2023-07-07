from django.db import models


class TrainerData(models.Model):
    user = models.ForeignKey(to='Users.User', on_delete=models.CASCADE, related_name='trainer_data')
    phone = models.CharField(max_length=120)
    certificates = models.ManyToManyField(to='Certificate', related_name='trainers')
    experience = models.DurationField()

    def __str__(self):
        return f"Trainer data of {self.user}"


class Certificate(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='certificate/')

    def __str__(self):
        return f"Certificate {self.title}"
