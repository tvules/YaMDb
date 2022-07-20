from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("user",),
        ("moderator"),
        ("admin"),
    ]
    username = models.CharField(db_index=True, max_length=150, unique=True)
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.CharField(null=True, blank=True)
    role = models.CharField(choices=ROLE_CHOICES, default="user")

    def __str__(self):
        return self.username
