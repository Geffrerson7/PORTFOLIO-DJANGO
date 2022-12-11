from django.urls import path
from .views import RegisterUser
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path(
        "logout/", LogoutView.as_view(template_name="user/logout.html"), name="logout"
    ),
    path('login/', LoginView.as_view(template_name="user/login.html"), name="login"),
]
