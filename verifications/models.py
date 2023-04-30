from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    url = models.CharField(max_length=100,default='' )
    # add additional fields in here

    def __str__(self):
        return self.username