# Generated by Django 4.0.4 on 2022-04-26 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_land_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='house_image',
            field=models.ImageField(blank=True, default=None, upload_to='house_images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='land',
            name='is_house',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='land',
            name='no_of_bedroom',
            field=models.IntegerField(blank=True, default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='land',
            name='no_of_washroom',
            field=models.IntegerField(blank=True, default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AddField(
            model_name='land',
            name='total_no_of_rooms',
            field=models.IntegerField(blank=True, default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
    ]