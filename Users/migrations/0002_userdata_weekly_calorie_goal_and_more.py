# Generated by Django 4.2.1 on 2023-06-05 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='weekly_calorie_goal',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='weekly_category_goal',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='weekly_exercise_goal',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Weights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weight', models.FloatField()),
                ('user_data_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weights', to='Users.userdata')),
            ],
        ),
        migrations.CreateModel(
            name='Heights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('height', models.FloatField()),
                ('user_data_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heights', to='Users.userdata')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercises.category')),
                ('user_data_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_categories', to='Users.userdata')),
            ],
        ),
        migrations.CreateModel(
            name='BurnedCalories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('calories', models.IntegerField()),
                ('user_data_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='burned_calories', to='Users.userdata')),
            ],
        ),
    ]
