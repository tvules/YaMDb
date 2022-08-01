from django.conf import settings
from django.core.exceptions import ValidationError


def validate_username(value):
    if value in settings.FORBIDDEN_NAMES:
        raise ValidationError(
            ('Выберете другое имя'),
        )
