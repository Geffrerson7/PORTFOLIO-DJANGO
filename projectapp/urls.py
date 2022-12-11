from django.urls import path
from .views import PortfolioView, ProjectCreate, ProjectDetailView
urlpatterns = [
    
    path('',PortfolioView.as_view(), name="index"),
    path('create/',ProjectCreate.as_view(), name="create"),
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name="detail"),
    
]