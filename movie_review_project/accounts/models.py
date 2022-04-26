from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator

from django.db import models

from movie_review_project.accounts.managers import MovieReviewUserManager
from movie_review_project.common.validators import validate_only_letters


class MovieReviewUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = MovieReviewUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 1
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MIN_LENGTH = 1
    LAST_NAME_MAX_LENGTH = 25

    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    date_of_birth = models.DateField(
        default='1920-01-01'
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS
    )

    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
    )

    image = models.ImageField(
        default='/images/default-profile-picture.jpg',
        upload_to='profile_images/',
    )

    user = models.OneToOneField(
        MovieReviewUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

