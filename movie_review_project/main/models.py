from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Avg

from movie_review_project.accounts.models import MovieReviewUser
from movie_review_project.common.validators import validate_star_rating


class Movie(models.Model):
    MAX_CHAR_FOR_MOVIE_NAME = 50
    MIN_CHAR_FOR_MOVIE_NAME = 1
    MAX_CHAR_FOR_MOVIE_GENRE = 25
    MIN_CHAR_FOR_MOVIE_GENRE = 4
    MAX_CHAR_FOR_MOVIE_DESCRIPTION = 100
    MAX_CHAR_FOR_MOVIE_ACTORS = 40

    movie_name = models.CharField(
        max_length=MAX_CHAR_FOR_MOVIE_NAME
    )

    date_release = models.DateField()

    genre = models.CharField(
        max_length=MAX_CHAR_FOR_MOVIE_GENRE,
        validators=(
            MinLengthValidator(MIN_CHAR_FOR_MOVIE_GENRE),
        )
    )

    movie_star_actors = models.CharField(max_length=MAX_CHAR_FOR_MOVIE_ACTORS)

    movie_description = models.CharField(max_length=MAX_CHAR_FOR_MOVIE_DESCRIPTION)

    movie_cover = models.ImageField(
        upload_to='movie_covers/',
    )

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_name

    def get_avg_rating(self):
        avg_rating = MovieReview.objects.filter(movie=self).aggregate(Avg('rating'))
        if avg_rating['rating__avg'] is None:
            return 0
        avg_rating = round(avg_rating['rating__avg'], 2)

        if avg_rating is not None:
            if avg_rating == 10:
                return 10

        return avg_rating

    class Meta:
        ordering = ['-date_added']


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

    rating = models.IntegerField(
        choices=RATING_CHOICES,
        validators=(
            validate_star_rating,
        )
    )

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie.movie_name

    class Meta:
        ordering = ['-date_added']


class Reviews(models.Model):

    author = models.ForeignKey(MovieReviewUser, on_delete=models.CASCADE)
    review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
