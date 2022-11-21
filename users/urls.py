from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.Registration.as_view(), name='register'),
    path('email-confirmation/<str:uidb64>/<str:token>/', 
          views.EmailConfirmation.as_view(), name="email-confirmation")
]
