from django.contrib import admin

from movie_review_project.main.models import Movie, MovieReview, Reviews


class MovieInlineAdmin(admin.StackedInline):
    model = Movie


class MovieReviewInlineAdmin(admin.StackedInline):
    model = MovieReview


class ReviewInlineAdmin(admin.StackedInline):
    model = Reviews


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'date_release')


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating')


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'review')
