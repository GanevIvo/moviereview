

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.utils import timezone

from movie_review_project.accounts.models import MovieReviewUser, Profile
from movie_review_project.main.forms import MovieReviewForm
from movie_review_project.main.models import Movie, MovieReview
from movie_review_project.main.views.movie_views import AddMovieReviewView

factory = RequestFactory()


class TestsAddMovieReview(TestCase):
    def setUp(self):
        self.client = Client()

        self.factory = RequestFactory()

        self.user = MovieReviewUser.objects.create_user(
            username='IvoGanev',
            password='ASD123fgh123',
            email='warriors123@abv.bg',
        )

        self.profile = Profile

        self.movie = Movie.objects.create(
            movie_name='Ted',
            date_release='1992-07-07',
            genre='Comedy',
            date_added='2011-07-07',
        )

        self.form_data = {
            'movie': self.movie,
            'content': 'Best movie',
            'rating': 10,
            'user': self.user,
        }

    def test_add_movie_review_form_is_valid(self):
        form = MovieReviewForm(data=self.form_data)
        self.assertTrue(form.is_valid())




