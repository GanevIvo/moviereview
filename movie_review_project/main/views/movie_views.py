from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from movie_review_project.main.forms import CreateMovieForm, MovieReviewForm, EditMovieReviewForm, DeleteMovieForm
from movie_review_project.main.models import Movie, MovieReview


class CreateMovieView(views.CreateView):
    form_class = CreateMovieForm
    template_name = 'admin_movie_templates/create-movie.html'
    success_url = reverse_lazy('reviews')


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

    def get_success_url(self):
        return reverse_lazy('reviews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class EditMovieReviewView(views.UpdateView):
    form_class = EditMovieReviewForm
    template_name = 'movie_templates/edit-movie-review.html'
    success_url = reverse_lazy('reviews')


class DeleteMovieReviewView(views.DeleteView):
    model = MovieReview
    template_name = 'movie_templates/delete-movie-review.html'
    success_url = reverse_lazy('reviews')
