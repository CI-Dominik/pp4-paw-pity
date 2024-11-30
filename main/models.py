from django.contrib.auth.models import AbstractUser
from django.db import models


# Define CustomUser so email is a unique field
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
