from django import forms
from django.contrib.auth import forms as auth_forms
from movie_review_project.common.mixins import BootstrapFormMixin
from movie_review_project.accounts.models import Profile
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

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'gender', 'date_of_birth']
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

            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                }
            )
        }


class DeleteProfileForm(BootstrapFormMixin, forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        MovieReview.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'
