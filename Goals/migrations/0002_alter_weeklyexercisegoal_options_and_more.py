# Generated by Django 4.2.1 on 2023-06-25 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weeklyexercisegoal',
            options={'ordering': ['-week']},
        ),
        migrations.RenameField(
            model_name='weeklyexercisegoal',
            old_name='exercise_goal',
            new_name='goal',
        ),
        migrations.RenameField(
            model_name='weeklyexercisegoal',
            old_name='last_date',
            new_name='week',
        ),
        migrations.AlterUniqueTogether(
            name='weeklyexercisegoal',
            unique_together=set(),
        ),
    ]