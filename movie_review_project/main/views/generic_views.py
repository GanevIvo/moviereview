from django.urls import reverse_lazy
from django.views import generic as views

from movie_review_project.main.forms import ReviewsForm
from movie_review_project.main.models import MovieReview, Movie


class HomeWithProfileView(views.TemplateView):
    template_name = 'main_templates/home-view-with-profile.html'
    success_url = reverse_lazy('home view with profile')
    extra_context = {'movie': Movie.objects.first()}


class HomeWithoutProfileView(views.TemplateView):
    template_name = 'main_templates/home-view-without-profile.html'
    success_url = reverse_lazy('home view without profile')
    extra_context = {'movie': Movie.objects.first()}


class Reviews(views.ListView):
    template_name = 'main_templates/movie-reviews.html'
    model = MovieReview
    form_class = ReviewsForm
