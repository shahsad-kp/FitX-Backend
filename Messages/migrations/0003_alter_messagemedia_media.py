# Generated by Django 4.2.1 on 2023-07-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0002_messagemedia_alter_message_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemedia',
            name='media',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
