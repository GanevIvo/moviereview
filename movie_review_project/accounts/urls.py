from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from movie_review_project.accounts.views import UserLoginView, UserLogoutView, CreateProfileView, EditProfileView, \
    DetailsProfileView, ChangeProfilePasswordView, DeleteProfileView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),

    path('profile/create', CreateProfileView.as_view(), name='create profile'),
    path('profile/edit/<int:pk>', EditProfileView.as_view(), name='edit profile'),
    path('profile/details/<int:pk>', DetailsProfileView.as_view(), name='details profile'),
    path('profile/change-password', ChangeProfilePasswordView.as_view(), name='change password'),
    path('profile/delete/<int:pk>', DeleteProfileView.as_view(), name='delete profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
