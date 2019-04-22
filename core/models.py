from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
def User(AbstractUser):
    name = models.CharField(max=5000)
