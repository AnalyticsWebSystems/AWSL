# urls.py
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('splash', views.splash, name='splash'),

    # Add similar URLs for signup, logout, etc.
]
