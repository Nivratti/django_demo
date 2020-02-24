from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Extending User Model Using a Custom Model Extending AbstractUser
    """
    avatar = models.FileField(upload_to='avatar', blank=True, null=True)
    
    # REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

