from django.shortcuts import render, redirect
# AuthenticationForm
from django.contrib.auth.models import User
#from django.contrib.auth import login, logout, authenticate
#from django.db import IntegrityError
from .forms import NewUserForm
from django.views.generic import CreateView

# Create your views here.



# def signup(request):
#     if request.method == "GET":
#         return render(request, "signup.html", {"form": UserCreationForm})
#     else:
#         if request.POST["password1"] == request.POST["password2"]:
#             try:
#                 user = User.objects.create_user(
#                     username=request.POST["username"],
#                     password=request.POST["password1"],
#                 )
#                 user.save()
#                 login(request, user)
#                 return redirect("tasks")
#             except IntegrityError:
#                 return render(
#                     request,
#                     "signup.html",
#                     {"form": UserCreationForm, "error": "User already exists"},
#                 )
#         return render(
#             request,
#             "signup.html",
#             {"form": UserCreationForm, "error": "Password do not match"},
#         )


# def signout(request):
#     logout(request)
#     return redirect("home")


# def signin(request):
#     if request.method == "GET":
#         return render(request, "signin.html", {"form": AuthenticationForm})
#     else:
#         user = authenticate(
#             request,
#             username=request.POST["username"],
#             password=request.POST["password"],
#         )
#         if user is None:
#             return render(
#                 request,
#                 "signin.html",
#                 {
#                     "form": AuthenticationForm,
#                     "error": "Username or password is incorrect",
#                 },
#             )
#         else:
#             login(request, user)
#             return redirect('tasks')
        
# def login(request):
#     context={}
#     context["form"]=LoginForm()
#     return render(request,"user/login.html",context)

class RegisterUser(CreateView):
    template_name = "user/register.html"
    form_class = NewUserForm

    def form_valid(self, form):
        form.save()
        return redirect("login")