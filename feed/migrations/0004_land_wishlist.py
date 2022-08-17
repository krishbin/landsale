# Generated by Django 4.0.4 on 2022-04-24 15:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0003_alter_land_options_rename_image_land_land_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='wishlist',
            field=models.ManyToManyField(blank=True, default=None, related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]