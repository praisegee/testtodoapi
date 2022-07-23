from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_create_user(self):
        user = User.objects.create_user(email="test@xample.com", password="test123")
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff, True)
        self.assertEqual(user.email, "test@xample.com")
        self.assertEqual(user.id, 1)
        self.assertEqual(user.__str__(), user.email)

    def test_create_superuser(self):
        user = User.objects.create_superuser(email="test@xample.com", password="test123")
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff, True)
        self.assertEqual(user.email, "test@xample.com")
        self.assertEqual(user.id, 1)

    def test_user_must_provide_an_email_and_password(self):
        self.assertRaises(ValueError, User.objects.create_user, email="", password="test123")
        self.assertRaises(ValueError, User.objects.create_user, email="test@xample.com", password="")

