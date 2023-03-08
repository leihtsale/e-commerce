from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):
    """
    Test for Custom User model
    """
    def test_creating_user_with_valid_email(self):
        """
        Creating a user with valid email
        should match the assigned email with the saved email
        """
        email = 'test@example.com'
        password = 'testpass1234'
        username = 'myusername'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_creating_user_without_email(self):
        """
        Creating a user without email
        should raise ValueError
        """
        email = ''
        password = 'testpass1234'
        username = 'myusername'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=email,
                password=password,
                username=username,
            )

    def test_creating_user_without_username(self):
        """
        Creating a user without username
        should raise ValueError
        """
        email = 'test@example.com'
        password = 'testpass1234'
        username = ''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=email,
                password=password,
                username=username,
            )

    def test_creating_superuser(self):
        """
        Creating a superuser
        should have attributes is_superuser and is_staff
        and must be equal to True
        """
        email = 'admin@example.com'
        password = 'admin1234'
        username = 'admin'
        admin = get_user_model().objects.create_superuser(
            email=email,
            password=password,
            username=username,
        )

        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
