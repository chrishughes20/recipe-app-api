from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

from core import models

class UserAdmin(BaseUserAdmin):
  ordering = ['id']
  list_display = ['email', 'name']
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    # Comma after 'name' is required with single fields:
    (_('Personal Info'), {'fields': ('name',)}),
    (
      _('Permissions'),
      {'fields': ('is_active', 'is_staff', 'is_superuser')}
    ),
    # Remember comma after 'last_login' since it is a single field:
    (_('Important dates'), {'fields': ('last_login',)})
  )
  add_fieldsets = (
    (None, {
      # Remember comma after 'wide' since it's a single field:
      'classes': ('wide',),
      'fields': ('email', 'password1', 'password2')
    }), # this comma is required since None is a single field
  )

admin.site.register(models.User, UserAdmin)