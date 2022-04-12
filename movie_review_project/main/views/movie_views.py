from django.urls import reverse_lazy
from django.views import generic as views

from movie_review_project.main.forms import CreateMovieForm, MovieReviewForm, EditMovieReviewForm
from movie_review_project.main.models import Movie, MovieReview


class CreateMovieView(views.CreateView):
    form_class = CreateMovieForm
    template_name = 'movie_templates/create-movie.html'
    success_url = reverse_lazy('reviews')


class DetailsMovieView(views.DeleteView):
    model = Movie
    template_name = 'movie_templates/details-movie.html'
    context_object_name = 'movie_name'


class AddMovieReviewView(views.UpdateView):
    form_class = MovieReviewForm
    template_name = 'movie_templates/add-movie-review.html'
    success_url = reverse_lazy('reviews')


class EditMovieReviewView(views.UpdateView):
    form_class = EditMovieReviewForm
    template_name = 'movie_templates/edit-movie-review.html'
    success_url = reverse_lazy('reviews')


class DeleteMovieReviewView(views.DeleteView):
    model = MovieReview
    template_name = 'movie_templates/delete-movie-review.html'
    success_url = reverse_lazy('reviews')

