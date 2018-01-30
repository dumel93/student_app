from datetime import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from .forms import UserLoginForm, UserCreateForm
from django.contrib.auth import authenticate, login, logout
from . import models

class UserLoginView(View):

    def get(self, request):
        form = UserLoginForm()
        ctx = {'form': form}
        return render(
            request,
            'accounts/login.html',
            ctx
        )

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('log')
        else:
            return render(
                request,
                'index.html',
                {'form': form}
            )


class UserCreateView(CreateView):
    form_class = forms.UserCreateForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('home')


class UserLogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('thanks')
        else:
            return redirect('log')

class UserEditView(UpdateView):
    model = models.User
    fields = ['username','email']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('log')

