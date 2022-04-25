from datetimewidget.widgets import DateWidget
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import PasswordChangeForm

from movie_review_project.common.mixins import BootstrapFormMixin
from movie_review_project.accounts.models import Profile, MovieReviewUser
from movie_review_project.main.models import MovieReview


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):

    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = auth_forms.get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['image'].help_text = ''

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'image']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Upload Image',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),

            'date_of_birth': DateWidget(
                attrs={
                    'min': '1920-01-01',
                }, usel10n=True, bootstrap_version=5
            )
        }


class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''


class DeleteProfileForm(BootstrapFormMixin, forms.ModelForm):
    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)

    def save(self, commit=True):
        MovieReview.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = MovieReviewUser
        fields = '__all__'
