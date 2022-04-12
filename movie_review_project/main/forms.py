from django import forms

from movie_review_project.accounts.models import Profile
from movie_review_project.main.models import MovieReview, Reviews, Movie


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['user', 'stars', 'content']


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['author', 'review']


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class EditMovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = '__all__'

