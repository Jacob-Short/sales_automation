from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django import forms
from authentication.forms import LoginForm, SignUpForm
from authentication.models import MyUser

from django.views.generic import View


def index_view(request):
    context = {}
    return render(request, 'index.html', context)



class LoginView(View):
    '''logs in registered user'''

    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'generic_form.html', context)


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                context = {}
                return HttpResponseRedirect(reverse('home'))



class SignUpView(View):
    '''creates form for new user to register'''

    def get(self, request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'generic_form.html', context)

    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['name'], password=data['password'])
        return HttpResponseRedirect(reverse('home'))


def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return render(request, 'index.html')

    
def profile_view(request, id):
    user = MyUser.objects.get(id=id)
    users_page = user
    context = {'users_page': users_page}
    return render(request, 'profile.html', context)

