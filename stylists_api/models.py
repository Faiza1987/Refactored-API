from django.db import models
from common.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class StylistProfile(User):
    stylist = models.OneToOneField(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="stylist_profile",
                                   parent_link=True)

    phone_number = models.CharField(max_length=10)
    years_experience = models.IntegerField(default=0)
    licenses = models.FileField(upload_to='uploads', blank=True)
    photo1 = models.ImageField(upload_to='uploads', blank=True)
    photo2 = models.ImageField(upload_to='uploads', blank=True)
    photo3 = models.ImageField(upload_to='uploads', blank=True)
    photo4 = models.ImageField(upload_to='uploads', blank=True)
    photo5 = models.ImageField(upload_to='uploads', blank=True)
    photo6 = models.ImageField(upload_to='uploads', blank=True)
    specializations = models.TextField(max_length=1000)