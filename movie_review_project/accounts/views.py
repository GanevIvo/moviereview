from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from movie_review_project.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from movie_review_project.accounts.models import Profile


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/accounts-login.html'
    success_url = reverse_lazy('home view with profile')

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    template_name = 'accounts/accounts-logout.html'
    success_url = reverse_lazy('home view without profile')


class CreateProfileView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/create-profile.html'
    success_url = reverse_lazy('home view with profile')


class EditProfileView(views.UpdateView):
    form_class = EditProfileForm
    model = Profile
    template_name = 'accounts/edit-profile.html'

    def get_success_url(self):
        profile_id = self.kwargs['pk']
        return reverse_lazy('details profile', kwargs={'pk': profile_id})


class DetailsProfileView(views.DetailView):
    template_name = 'accounts/details-profile.html'
    model = Profile


class ChangeProfilePasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change-profile-password.html'


class DeleteProfileView(views.DeleteView):
    template_name = 'accounts/delete-profile.html'
    form_class = DeleteProfileForm
    model = Profile

    success_url = reverse_lazy('home view without profile')
