from django.test import TestCase
from django.contrib.auth import get_user_model

# docker-compose run app sh -c "python manage.py test"
# docker-compose run app sh -c "python manage.py makemigrations core"

class ModelTests(TestCase):

  def test_create_user_with_email_successful(self):
    '''Test creating a new user with an email is successful'''
    email = 'test@test.com'
    password = 'test123'
    user = get_user_model().objects.create_user(
      email = email,
      password = password
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalize(self):
    '''Test the email for new user is normalized'''
    email = 'test@TEST.com'
    user = get_user_model().objects.create_user(email, 'test123')

    self.assertEqual(user.email, email.lower())

  def test_new_user_invalid_email(self):
    '''Test creating user with no email raises error'''
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, 'test123')

  def test_create_new_super_user(self):
    '''Test creating a new super user'''
    user = get_user_model().objects.create_superuser(
      'test@test.com',
      'test123'
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)