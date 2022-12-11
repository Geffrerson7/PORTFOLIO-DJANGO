from django.shortcuts import render, redirect
# AuthenticationForm
from django.contrib.auth.models import User
#from django.contrib.auth import login, logout, authenticate
#from django.db import IntegrityError
from .forms import NewUserForm
from django.views.generic import CreateView

# Create your views here.

class RegisterUser(CreateView):
    template_name = "user/register.html"
    form_class = NewUserForm

    def form_valid(self, form):
        form.save()
        return redirect("login")