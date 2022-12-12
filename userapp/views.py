from django.shortcuts import render, redirect
# AuthenticationForm
from django.contrib.auth.models import User
#from django.contrib.auth import login, logout, authenticate
#from django.db import IntegrityError
from .forms import NewUserForm
from django.views.generic import CreateView
from django.contrib import messages

# Create your views here.


class RegisterUser(CreateView):
    template_name = "user/register.html"
    form_class = NewUserForm

    def form_valid(self, form):
        
        if form.is_valid():
            form.save()
            messages.success(self.request, 'User created')
        else:
            messages.error(self.request, 'Error creating user')
        return redirect("register")