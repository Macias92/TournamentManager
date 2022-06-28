from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import LoginForm, CreateUserForm
from django.contrib.auth.models import User
from django.urls import reverse

from accounts.models import Profile


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                redirect_url = request.GET.get('next', '/')
                # pobierze co jest w url po 'next' i tam bedzie przekierowywać, jeżeli tego nie ma to przekierowuje na '/'
                return redirect(redirect_url)
            else:
                return render(request, 'form.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class CreateUserView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        errors = []
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            birth_date = form.cleaned_data.get('birth_date')
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            if not password == password2:
                errors.append('Passwords are not the same, please try again!')
            if email and User.objects.filter(email=email).exists():
                errors.append('User with that email exist, please use different email address!')
            if len(errors) == 0:
                user = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                username=username,
                                                email=email,
                                                password=password)
                profile = Profile(user=user, birth_date=birth_date)
                profile.save()
                return redirect(reverse('login'))
            return render(request, 'form.html', context={'errors': errors})

