
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User, Cart

class UserAdmin(BaseUserAdmin):

  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (_('Personal Info'), {'fields': ('first_name', 'last_name', 'phone_no')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
  )
  list_display = ['email', 'is_staff', 
                  "first_name", "last_name", "phone_no"]
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email', )
admin.site.register(User, UserAdmin)
admin.site.register(Cart)