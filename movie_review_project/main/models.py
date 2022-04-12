from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from movie_review_project.accounts.models import MovieReviewUser
from movie_review_project.common.validators import validate_only_letters, validate_only_alphanumeric, \
    validate_star_rating


class Movie(models.Model):
    MAX_CHAR_FOR_MOVIE_NAME = 50
    MIN_CHAR_FOR_MOVIE_NAME = 1
    MAX_CHAR_FOR_MOVIE_GENRE = 25
    MIN_CHAR_FOR_MOVIE_GENRE = 4

    movie_name = models.CharField(
        max_length=MAX_CHAR_FOR_MOVIE_NAME,
        validators=(
            MinLengthValidator(MIN_CHAR_FOR_MOVIE_NAME),
            validate_only_alphanumeric,
        )
    )

    date_release = models.DateField()

    genre = models.CharField(
        max_length=MAX_CHAR_FOR_MOVIE_GENRE,
        validators=(
            MinLengthValidator(MIN_CHAR_FOR_MOVIE_GENRE),
            validate_only_letters,
        )
    )

    movie_star_actors = models.TextField()

    movie_description = models.TextField()

    movie_cover = models.ForeignKey('MovieImage', on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name


class MovieImage(models.Model):
    image = models.ImageField(upload_to='mediafiles/')
    user = models.ForeignKey(MovieReviewUser, on_delete=models.CASCADE)


class MovieReview(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(MovieReviewUser, on_delete=models.CASCADE)

    content = models.TextField(
        blank=True,
        null=True
    )

    stars = models.IntegerField(
        choices=RATING_CHOICES,
        validators=(
            validate_star_rating,
        )
    )

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie.movie_name


class Reviews(models.Model):

    author = models.ForeignKey(MovieReviewUser, on_delete=models.CASCADE)
    review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
