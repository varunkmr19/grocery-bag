from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegistrationView.as_view(), name='register'),
    path('logout', views.LogoutView.as_view(), name='logout')
]
