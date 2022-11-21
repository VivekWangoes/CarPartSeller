from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('contact/',views.ContactForm.as_view(), name='contact'),
    path('about-us/',views.AboutUs.as_view(), name='about-us'),
    path('',views.Parts.as_view(), name='parts'),
    path('parts-details/<uuid:pk>/',views.PartDetail.as_view(), name='parts-details'),
    path('add_parts/',views.AddPart.as_view(),name='add_parts'),
    path('add_to_cart/<uuid:pk>/', views.AddToCart.as_view(), name="add_to_cart")
]
