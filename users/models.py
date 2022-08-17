from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image
from django.db import models

class CustomUser(AbstractUser):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_UNKNOWN = 'U'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),(GENDER_UNKNOWN, 'Unknown')]
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    phone_number = PhoneNumberField()
    location = models.CharField(max_length=50)
    profile_picture = models.ImageField(default='default.jpg',upload_to='profile_picture/')

    def get_phone_number(self):
        return self.phone_number

    def get_gender(self):
        return self.gender

    def save(self,*args,**kwargs):
        super().save()
        image = Image.open(self.profile_picture.path)
        if image.height > 300:
            aspect_ratio = image.height/image.width
            image.thumbnail((300/aspect_ratio,300))
            image.save(self.profile_picture.path)

    def __str__(self):
        return self.username
