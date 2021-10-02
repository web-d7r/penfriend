from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse

from .models import Profile
from .forms import ProfileForm, RegistrationForm
from .views import IndexView, UserCreateView, Login

# Create your tests here.

# Testing 'Profile' Model
class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='Bill', last_name='Gates')

    def test_about_me_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('about_me').max_length
        self.assertEqual(max_length, 300)

    def test_about_me_blank(self):
        profile = Profile.objects.get(id=1)
        blank = profile._meta.get_field('about_me').blank
        self.assertEqual(blank, True)

    def test_gender_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('gender').max_length
        self.assertEqual(max_length, 1)

    def test_city_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('city').max_length
        self.assertEqual(max_length, 30)

# Testing ProfileForm
class ProfileFormTest(TestCase):
    def test_empty_form(self):
        form = ProfileForm()
        self.assertIn('gender', form.fields)
        self.assertIn('birth_date', form.fields)
        self.assertIn('about_me', form.fields)
        self.assertIn('country', form.fields)
        self.assertIn('city', form.fields)

# Testing RegistrationForm
class RegistrationFormTest(TestCase):
    def test_empty_form(self):
        form = RegistrationForm()
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)

class TestPages(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index(self):
        # Create an instance of a GET request.
        request = self.factory.get(reverse('index'))
        request.user = AnonymousUser()
        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_registration_page(self):
        request = self.factory.get(reverse('registration'))
        request.user = AnonymousUser()
        response = UserCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        request = self.factory.get(reverse('login'))
        request.user = AnonymousUser()
        response = Login.as_view()(request)
        self.assertEqual(response.status_code, 200)







