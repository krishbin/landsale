from django.db import models
from users.models import CustomUser
from django.urls import reverse
from django.shortcuts import redirect
from django.core.validators import MinValueValidator,MaxValueValidator,EMPTY_VALUES
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Land(models.Model):
    BIGHA = 'BG'
    KATTHA = 'KT'
    ROPANI = 'RO'
    AANA = 'AN'
    SQUAREMILE = 'SM'
    SQUAREFEET = 'SF'
    LAND_AREA_CHOICES = [
        (BIGHA, 'Bigha'),
        (KATTHA, 'Kattha'),
        (ROPANI, 'Ropani'),
        (AANA, 'Aana'),
        (SQUAREFEET, 'SquareFeet'),
        (SQUAREMILE, 'SquareMile'),
    ]
    location = models.CharField(max_length=30)
    info = models.TextField()
    area = models.FloatField()
    area_unit = models.CharField(
        max_length=2,
        choices=LAND_AREA_CHOICES,
        default=AANA,
    )
    longitude = models.FloatField()
    latitude = models.FloatField()
    land_image = models.ImageField(upload_to = 'land_images/%Y/%m/%d/')
    landownership_image = models.ImageField(upload_to = 'ownership_images/%Y/%m/%d/')
    landownership_image_optional = models.ImageField(upload_to = 'ownership_images/%Y/%m/%d/',blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    verified = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    wishlist = models.ManyToManyField(CustomUser, default=None, blank=True, related_name='wishlist')
    is_house_or_apartment = models.BooleanField(default=False)
    total_no_of_rooms = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(30)],blank=True,default=0)
    no_of_bedroom = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=True,default=0)
    no_of_washroom = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(15)],blank=True,default=0)
    house_image = models.ImageField(upload_to = 'house_images/%Y/%m/%d/',blank=True,default=None)

    def clean(self):
        if self.is_house_or_apartment:
            if self.total_no_of_rooms in EMPTY_VALUES:
                raise ValidationError(_('Total no of rooms is required'))
            if self.no_of_bedroom in EMPTY_VALUES:
                raise ValidationError(_('No of bedroom is required'))
            if self.no_of_washroom in EMPTY_VALUES:
                raise ValidationError(_('No of washroom is required'))
            if self.house_image in EMPTY_VALUES:
                raise ValidationError(_('House image is required'))

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('detail-land',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-date_posted']
