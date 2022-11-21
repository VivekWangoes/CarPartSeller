from django.db import models
from base.models import BaseModel
from base.utils import generate_ref_code

class GalleryImage(BaseModel):
    images = models.ImageField(
        upload_to='gallery_image/', 
        blank=True, 
        null=True)


class ProductDetail(BaseModel):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.ImageField(
            upload_to='product/', 
            blank=True, 
            null=True)
    vin = models.CharField(max_length=17, blank=True, null=True, unique=True)
    info = models.TextField(blank=True, null=True)
    gallery_image = models.ManyToManyField(GalleryImage, blank=True)


    def save(self, *args, **kwargs):
        vin_number = generate_ref_code()
        self.vin = vin_number
        super(ProductDetail, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Contact(BaseModel):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=1000, blank=True, null=True)
    message = models.TextField(blank=True, null=True)