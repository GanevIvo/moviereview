from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_review_project.main.urls')),
    path('', include('movie_review_project.accounts.urls')),
]


