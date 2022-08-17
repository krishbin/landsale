from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from .models import CustomUser
from django.db import models

class CustomUserCreationForm(UserCreationForm):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_UNKNOWN = 'U'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),(GENDER_UNKNOWN, 'Unknown')]
    location = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    profile_picture = models.ImageField(default='default.jpg',upload_to='profile_picture/')
    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2','gender','phone_number','location','profile_picture']

class CustomUserChangeForm(UserChangeForm):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_UNKNOWN = 'U'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),(GENDER_UNKNOWN, 'Unknown')]
    location = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_picture/')
    password = None
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','gender','phone_number','location','profile_picture']

class RegistrationForm(UserCreationForm):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_UNKNOWN = 'U'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),(GENDER_UNKNOWN, 'Unknown')]
    phone_number = PhoneNumberField()
    email = forms.EmailField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    profile_picture = models.ImageField(default='default.jpg',upload_to='profile_picture/')

    def clean_first_name(self):
        if self.cleaned_data["first_name"].strip() == '':
            raise ValidationError("First name is required.")
        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        if self.cleaned_data["last_name"].strip() == '':
            raise ValidationError("Last name is required.")
        return self.cleaned_data["last_name"]

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','gender','phone_number','location','password1','password2','profile_picture']
