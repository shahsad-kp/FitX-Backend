# Generated by Django 4.2.1 on 2023-06-06 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_data',
        ),
        migrations.AddField(
            model_name='user',
            name='weekly_calorie_goal',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weekly_category_goal',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weekly_exercise_goal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='burnedcalorie',
            name='user_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='burned_calories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='completedcategory',
            name='user_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='height',
            name='user_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heights', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='weight',
            name='user_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weights', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
