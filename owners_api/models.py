from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from common.models import User


class OwnerProfile(User):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name="salon_profile",
                                 parent_link=True)

    salon_name = models.CharField(max_length=20)
    salon_address = models.CharField(max_length=255)
    salon_city = models.CharField(max_length=255)
    salon_state = models.CharField(max_length=2)
    salon_zip = models.CharField(max_length=5)
    salon_phone_number = models.CharField(max_length=10)
    salon_description = models.TextField(max_length=2000)