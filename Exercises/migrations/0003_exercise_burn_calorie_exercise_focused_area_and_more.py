# Generated by Django 4.2.1 on 2023-06-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0002_alter_exercise_count_alter_exercise_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='burn_calorie',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='focused_area',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='video_link',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
