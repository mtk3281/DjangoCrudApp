from django.contrib.auth.models import AbstractUser
from django.db import models

#! creating a custom user model with additional name and DOB option while registering
class CustomUser(AbstractUser):
    name = models.CharField(blank=False,null=False, max_length=255)
    dob = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)