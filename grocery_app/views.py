from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'grocery_app/layout.html')


def login_view(request):
    return render(request, 'grocery_app/login.html')


def signup_view(request):
    return render(request, 'grocery_app/signup.html')
