from django.shortcuts import redirect  
from django.contrib.auth.models import User

from .forms import NewUserForm
from django.views.generic import CreateView
from django.contrib import messages

# Create your views here.

class RegisterUser(CreateView):
    template_name = "user/register.html"
    form_class = NewUserForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "User created")
        return redirect("register")
