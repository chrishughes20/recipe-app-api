from django.test import TestCase

from app.calc import add, subtract


# docker-compose run app sh -c "python manage.py test && flake8"

class CalcTests(TestCase):
  
  # Test functions must begin with test:
  def test_add_numbers(self):
    '''Test sum of two numbers'''
    self.assertEqual(add(3,8), 11)

  def test_subtract_numbers(self):
    '''Test difference of two numbers'''
    self.assertEqual(subtract(5,11), 6)