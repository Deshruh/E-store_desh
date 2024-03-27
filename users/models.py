from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
    status = models.TextField(null=True, blank=True)
<<<<<<< HEAD
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
=======
    phone_number = models.PositiveIntegerField(null=True, blank=True)
>>>>>>> e0ea8df6e5c80f6970e106a9500bf4df3f1aefdb
    # staff = models.CharField(max_length=50)
    # pay_card = ...