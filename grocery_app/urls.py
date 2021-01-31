from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegistrationView.as_view(), name='register'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('item/add', views.AddItem.as_view(), name='add'),
    path('item/<int:pk>/update', views.UpdateItem.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteItem.as_view(), name='delete'),
    path('home', views.filter_by_date, name='filter')
]
