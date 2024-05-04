# urls.py
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),

    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),

    path('splash/', views.splash, name='splash'),

    # Add similar URLs for signup, logout, etc.
]
