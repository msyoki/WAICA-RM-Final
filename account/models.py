from datetime import date
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from pytz import country_names
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, first_name, password, **other_fields):

        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_admin') is not True:
            raise ValueError(
                'Superuser must be assigned to is_admin=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, first_name, password, **other_fields)

    def create_user(
            self,
            email,
            first_name,
            password,
            last_name,
            country,
            **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            country=country,
            **other_fields)
        user.set_password(password)
        user.save()
        return user


COUNTRIES = (
    ('HQ', 'HQ'),  # Sierra Leone
    ('KE', 'KE'),  # Kenya
    ('ZW', 'ZW'),  # Zimbabwe
    ('NG', 'NG'),  # Nigeria
    ('TN', 'TN'),  # Tunisia
    ('GH', 'GH'),  # Ghana
    ('CIV', 'CIV'),  # Ivory Coast
)

LANGUAGE_CHOICES = (
    ('en-us', 'English'),
    ('fr', 'French'),
)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    language = models.CharField(
        default='en-us',
        choices=LANGUAGE_CHOICES,
        max_length=5)
    country = models.CharField(
        max_length=60, choices=COUNTRIES,)
    start_date = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'country']

    def __str__(self):
        return f"Admin:{self.is_admin}-{self.first_name} {self.last_name} - {self.email} "

    @property
    def is_staff(self):
        return self.is_admin


class UserActivityLog(models.Model):

    date = models.DateField(auto_now_add=True)
    time =  models.TimeField(auto_now_add=True)
    user_email = models.EmailField(max_length=500)
    user_name = models.CharField(default="None",max_length=500,blank=True,null=True)
    ip_address = models.CharField(max_length=500)
    activity = models.CharField(max_length=500)
    country = models.CharField(default="None", max_length=500)
   
    class Meta:
       ordering = ('-date','-time')
       

    def __str__(self):
        return f'({self.date} - {self.time} - {self.activity} - {self.ip_address} - {self.user_email} -  {self.user_name} - {self.country})'