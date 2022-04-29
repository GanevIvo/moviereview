from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from movie_review_project.accounts.models import MovieReviewUser


class CreateProfileViewTests(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = MovieReviewUser.objects.create_user(
            username='IvoGanev',
            password='ASD123fgh123',
            email='warriors123@abv.bg',
        )

    def test_get_CreateProfile_expect_correct_template(self):
        response = self.test_client.get(reverse('create profile'))

        self.assertTemplateUsed(response, 'accounts/create-profile.html')

    def test_CreateProfile_when_creating_is_valid_should_create_the_profile(self):
        data = {
            'username': 'IvoGanev',
            'password1': 'ASD123fgh123',
            'password2': 'ASD123fgh123',
            'email': 'warriors123@abv.bg'
        }

        self.test_client.post(
            reverse('create profile'),
            data=data,
        )

        profile = MovieReviewUser.objects.get()
        self.assertIsNotNone(profile)
        self.assertEqual(data['username'], profile.username)
        self.assertEqual(data['email'], profile.email)

