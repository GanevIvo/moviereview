from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from movie_review_project.main.views.generic_views import Reviews, HomeWithProfileView, HomeWithoutProfileView
from movie_review_project.main.views.movie_views import CreateMovieView, AddMovieReviewView, EditMovieReviewView, \
    DeleteMovieReviewView, DetailsMovieView

urlpatterns = [
    path('', HomeWithoutProfileView.as_view(), name='home view without profile'),
    path('home/', HomeWithProfileView.as_view(), name='home view with profile'),
    path('reviews/', Reviews.as_view(), name='reviews'),

    path('movie/create', CreateMovieView.as_view(), name='create movie'),
    path('movie/details/<int:pk>', DetailsMovieView.as_view(), name='details movie'),

    path('movie/add-review', AddMovieReviewView.as_view(), name='add movie review'),
    path('movie/edit-review/<int:pk>', EditMovieReviewView.as_view(), name='edit movie review'),
    path('movie/delete-review/<int:pk>', DeleteMovieReviewView.as_view(), name='delete movie review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
