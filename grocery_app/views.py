from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'grocery_app/layout.html')


class LoginView(View):
    def post(self, request):
        # Attempt to sign user in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'grocery_app/login.html', {
                'error': 'Invalid username and/or password.'
            })

    def get(self, request):
        return render(request, 'grocery_app/login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


def signup_view(request):
    return render(request, 'grocery_app/signup.html')
