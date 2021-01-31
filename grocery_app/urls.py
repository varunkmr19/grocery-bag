from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('signup', views.signup_view, name='signup'),
    path('logout', views.LogoutView.as_view(), name='logout')
]
