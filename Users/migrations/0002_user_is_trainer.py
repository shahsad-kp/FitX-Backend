# Generated by Django 4.2.1 on 2023-07-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_trainer',
            field=models.BooleanField(default=False),
        ),
    ]