# Generated by Django 2.1 on 2019-02-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_remove_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, upload_to='carsf'),
        ),
    ]
