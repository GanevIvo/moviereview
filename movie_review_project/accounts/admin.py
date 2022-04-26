from django.contrib import admin

from movie_review_project.accounts.models import Profile, MovieReviewUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(MovieReviewUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff')
