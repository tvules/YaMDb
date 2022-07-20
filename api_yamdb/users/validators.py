from django.core.exceptions import ValidationError

forbidden_names = ['me', 'admin', 'moderator']


def validate_username(value):
    if value in forbidden_names:
        raise ValidationError(
            ('%(value)s выберете другое имя'),
            params={'value': value},
        )
