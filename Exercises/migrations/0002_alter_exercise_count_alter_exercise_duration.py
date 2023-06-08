# Generated by Django 4.2.1 on 2023-06-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='duration',
            field=models.DurationField(null=True),
        ),
    ]
