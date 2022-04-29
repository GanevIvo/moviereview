from django.core.exceptions import ValidationError


def validate_only_letters(value):

    if not all(ch.isalpha() for ch in value):
        raise ValidationError('Must contain only letters')


def validate_only_alphanumeric(value):
    if not all(ch.isalnum() for ch in value):
        raise ValidationError('Must contain only letters and numbers')


def validate_star_rating(value):
    if value > 10:
        raise ValueError('The value must be below or equal to 10')

    if value < 1:
        raise ValueError('The value must be at least 1')
