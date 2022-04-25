from django import forms

from movie_review_project.common.mixins import BootstrapFormMixin, DisabledFieldsFormMixin
from movie_review_project.main.models import MovieReview, Reviews, Movie


class MovieReviewForm(forms.ModelForm):

    class Meta:
        model = MovieReview
        fields = '__all__'
        exclude = ['user',]


class EditMovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = '__all__'


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['author', 'review']


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class DeleteMovieForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Movie
        exclude = ('user_profile',)
