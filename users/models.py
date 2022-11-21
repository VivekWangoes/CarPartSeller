from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel
from .managers import CustomUserManager
from parts.models import ProductDetail

class User(BaseModel, AbstractUser):
  username = models.CharField(max_length=100, blank=True, null=True)
  email = models.EmailField(unique = True)
  first_name = models.CharField(max_length=100, blank=True, null=True)
  last_name = models.CharField(max_length=100, blank=True, null=True)
  phone_no = models.CharField(max_length=10, blank=True, null=True)
  is_active = models.BooleanField(default=False)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  object = CustomUserManager()


  def __str__(self):
      return "{}".format(self.email)


class Cart(BaseModel):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  product = models.ManyToManyField(ProductDetail)
  is_puchase = models.BooleanField(default=False)


  def get_total_price(self):
    data = sum([i.price for i in self.product.all()])
    return data