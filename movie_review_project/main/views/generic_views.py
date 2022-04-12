from django.urls import reverse_lazy
from django.views import generic as views

from movie_review_project.main.forms import ReviewsForm
from movie_review_project.main.models import MovieReview


class HomeWithProfileView(views.TemplateView):
    template_name = 'main_templates/home-view-with-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context

    success_url = reverse_lazy('home view with profile')


class HomeWithoutProfileView(views.TemplateView):
    template_name = 'main_templates/home-view-without-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context

    success_url = reverse_lazy('home view without profile')


class Reviews(views.ListView):
    template_name = 'main_templates/movie-reviews.html'
    model = MovieReview
    form_class = ReviewsForm
