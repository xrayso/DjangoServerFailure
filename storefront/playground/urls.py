from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path("dashboard/", views.dashboard_view, name='dashboard'),
    path("add_money", views.add_money, name='add_money'),
]