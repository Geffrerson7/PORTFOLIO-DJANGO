from django.urls import path
from .views import (
    PortfolioView,
    ProjectCreate,
    ProjectDetailView,
    deleteProject,
    rick_y_morty_View,
    fin_de_unidad_1_View,
)

urlpatterns = [
    path("", PortfolioView.as_view(), name="index"),
    path("create/", ProjectCreate.as_view(), name="create"),
    path("detail/<int:pk>/", ProjectDetailView.as_view(), name="detail"),
    path("delete/<int:id>/", deleteProject, name="delete"),
    path("detail/rick-y-morty/", rick_y_morty_View, name="rick-y-morty"),
    path("detail/fin-de-unidad-1/", fin_de_unidad_1_View, name="fin-de-unidad-1"),
]
