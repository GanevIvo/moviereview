from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from movie_review_project.main.views.generic_views import Reviews, HomeWithProfileView, HomeWithoutProfileView
from movie_review_project.main.views.movie_views import CreateMovieView, AddMovieReviewView, EditMovieReviewView, \
    DeleteMovieReviewView, MoviesView, MoviesDetailsView, DeleteMovieView

urlpatterns = [
    path('', HomeWithoutProfileView.as_view(), name='home view without profile'),
    path('home/', HomeWithProfileView.as_view(), name='home view with profile'),
    path('movies/', MoviesView.as_view(), name='movies'),
    path('movies/details/<int:pk>', MoviesDetailsView.as_view(), name='movies details'),
    path('movies/delete/<int:pk>', DeleteMovieView.as_view(), name='delete movie'),
    path('reviews/', Reviews.as_view(), name='reviews'),

    path('movie/create', CreateMovieView.as_view(), name='create movie'),

    path('movie/add-review/<int:pk>', AddMovieReviewView.as_view(), name='add movie review'),
    path('movie/edit-review/<int:pk>', EditMovieReviewView.as_view(), name='edit movie review'),
    path('movie/delete-review/<int:pk>', DeleteMovieReviewView.as_view(), name='delete movie review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
