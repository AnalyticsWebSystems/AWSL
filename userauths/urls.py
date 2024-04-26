# urls.py
from django.urls import path
from . import views

app_name = "userauths"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),

    path('register/', views.register, name='register'),

    # Add similar URLs for signup, logout, etc.
]
