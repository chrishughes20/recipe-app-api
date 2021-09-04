from django.test import TestCase

from app.calc import add


# docker-compose run app sh -c "python manage.py test"

class CalcTests(TestCase):
  
  # Test functions must begin with test:
  def test_add_numbers(self):
    '''Test sum of two numbers'''
    self.assertEqual(add(3,8), 11)