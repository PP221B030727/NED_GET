from email.policy import default

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
#

class User(AbstractUser):
    phone_number = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)   #поле мжт быть пустым blank True
