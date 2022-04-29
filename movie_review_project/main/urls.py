from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from movie_review_project.main.views.generic_views import Reviews, HomeWithProfileView, HomeWithoutProfileView
from movie_review_project.main.views.movie_views import CreateMovieView, AddMovieReviewView, MoviesView, \
    MoviesDetailsView, DeleteMovieView, EditMovieReviewView, DeleteMovieReviewView, EditMovieView

handler404 = 'movie_review_project.main.views.movie_views.custom_page_not_found_view'
handler500 = 'movie_review_project.main.views.movie_views.custom_error_view'

urlpatterns = [
    path('', HomeWithoutProfileView.as_view(), name='home view without profile'),
    path('home/', HomeWithProfileView.as_view(), name='home view with profile'),

    path('movies/', MoviesView.as_view(), name='movies'),
    path('movie/create', CreateMovieView.as_view(), name='create movie'),
    path('movie/edit/<int:pk>', EditMovieView.as_view(), name='edit movie'),
    path('movies/details/<int:pk>', MoviesDetailsView.as_view(), name='movies details'),
    path('movies/delete/<int:pk>', DeleteMovieView.as_view(), name='delete movie'),

    path('reviews/', Reviews.as_view(), name='reviews'),
    path('movie/add-review/<int:pk>', AddMovieReviewView.as_view(), name='add movie review'),
    path('movie/edit-review/<int:pk>', EditMovieReviewView.as_view(), name='edit movie review'),
    path('movie/delete-review/<int:pk>', DeleteMovieReviewView.as_view(), name='delete movie review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


