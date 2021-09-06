from django.test import TestCase, Client, client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

  def setUp(self):
    self.client = Client()
    self.admin_user = get_user_model().objects.create_superuser(
      email = 'admin@test.com',
      password = 'test123'
    )
    self.client.force_login(self.admin_user)
    self.user = get_user_model().objects.create_user(
      email = 'test@test.com',
      password = 'test123',
      name = 'Test Name'
    )
  
  def test_users_listed(self):
    '''Test that users are listed on users page'''
    url = reverse('admin:core_user_changelist')
    # Response: use get request:
    res = self.client.get(url)
    
    self.assertContains(res, self.user.name)
    self.assertContains(res, self.user.email)

  def test_user_change_page(self):
    '''Tests that the user edit page works'''
    # Generates URL like /admin/core/user:1 (1 being user ID):
    url = reverse('admin:core_user_change', args=[self.user.id])
    res = self.client.get(url)

    self.assertEqual(res.status_code, 200)

  def test_create_user_page(self):
    '''Test that the create user page works'''
    url = reverse('admin:core_user_add')
    res = self.client.get(url)
    
    self.assertEqual(res.status_code, 200)