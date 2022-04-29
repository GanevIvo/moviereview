from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from movie_review_project.main.forms import CreateMovieForm, MovieReviewForm, DeleteMovieForm, EditMovieReviewForm, \
    DeleteMovieReviewForm, EditMovieForm
from movie_review_project.main.models import Movie, MovieReview


def custom_page_not_found_view(request, exception):
    return render(request, "error-404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "error-500.html", {})


class CreateMovieView(views.CreateView):
    form_class = CreateMovieForm
    template_name = 'admin_movie_templates/create-movie.html'

    def get_success_url(self):
        return reverse_lazy('reviews')


class EditMovieView(views.UpdateView):
    model = Movie
    template_name = 'admin_movie_templates/edit-movie.html'
    form_class = EditMovieForm

    def get_success_url(self):
        return reverse_lazy('movies')


class DeleteMovieView(views.DeleteView):
    template_name = 'admin_movie_templates/delete-movie.html'
    form_class = DeleteMovieForm
    model = Movie

    def get_success_url(self):
        return reverse_lazy('movies')


class MoviesView(views.ListView):
    model = Movie
    template_name = 'movie_templates/movies.html'
    context_object_name = 'movie'
    extra_context = {'movie_review': MovieReview.objects.all()}


class MoviesDetailsView(views.DetailView):
    template_name = 'movie_templates/movies-details.html'
    model = Movie
    context_object_name = 'movie'


class AddMovieReviewView(views.CreateView):
    form_class = MovieReviewForm
    template_name = 'movie_templates/add-movie-review.html'
    model = MovieReview

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddMovieReviewView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('reviews')


class EditMovieReviewView(views.UpdateView):
    model = MovieReview
    form_class = EditMovieReviewForm
    template_name = 'movie_templates/edit-movie-review.html'

    def get_success_url(self):
        return reverse_lazy('reviews')


class DeleteMovieReviewView(views.DeleteView):
    model = MovieReview
    form_class = DeleteMovieReviewForm
    template_name = 'movie_templates/delete-movie-review.html'

    def get_success_url(self):
        return reverse_lazy('reviews')
