from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from .validators import validate_username

ROLE_CHOICES = [
    ("user", "user"),
    ("moderator", "moderator"),
    ("admin", "admin"),
]


class User(AbstractUser):
    username = models.CharField(
        db_index=True,
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator, validate_username]
    )
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.CharField(null=True, blank=True, max_length=150)
    role = models.CharField(
        choices=ROLE_CHOICES, default="user", max_length=15)
    confirmation_code = models.CharField(
        editable=False, max_length=50, blank=True)

    def __str__(self):
        return self.username
