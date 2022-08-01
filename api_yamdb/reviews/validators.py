import datetime as dt

from django.core.exceptions import ValidationError

INVALID_YEAR = "Год должен быть между {min_year} и {max_year}"
MIN_YEAR = -1000
MAX_YEAR = dt.datetime.now().year


def validate_year(value):
    if value < MIN_YEAR or value > MAX_YEAR:
        raise ValidationError(
            INVALID_YEAR.format(min_year=MIN_YEAR, max_year=MAX_YEAR)
        )
