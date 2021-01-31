from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import User, Item

# Create your views here.


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            # get grocery list
            grocery_list = Item.objects.filter(owner=request.user).all()

            return render(request, 'grocery_app/index.html', {
                'grocery': grocery_list
            })
        else:
            return HttpResponseRedirect(reverse('login'))


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


class RegistrationView(View):
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirm-password']
        if password != confirmation:
            return render(request, 'grocery_app/register.html', {
                'error': 'Passwords must match.'
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username, email, password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
        except IntegrityError:
            return render(request, 'grocery_app/register.html', {
                'error': 'Username already taken.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    def get(self, request):
        return render(request, 'grocery_app/register.html')


class AddItem(LoginRequiredMixin, View):
    def post(self, request):
        # create new item
        name = request.POST['item_name']
        quantity = request.POST['quantity']
        date = request.POST['date']
        status = request.POST['status']

        new_item = Item(
            owner=request.user,
            name=name,
            quantity=quantity,
            status=status,
            date=date
        )
        new_item.save()

        return HttpResponseRedirect(reverse('index'))

    def get(self, request):
        return render(request, 'grocery_app/add.html')
