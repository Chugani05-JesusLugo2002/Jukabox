from django.core.exceptions import ValidationError
from datetime import datetime

def validate_year_range(value: int):
    current_year = datetime.now().year
    if not 1900 < value < current_year:
        raise ValidationError(
            f'Year needs between 1900 and {current_year}.'
        )