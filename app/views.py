from django.shortcuts import render
from .models import Project, Technology


# Create your views here.
def index(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()

    return render(request, "app/index.html", {
        "projects": projects,
        "technologies": technologies,
    })


def splash(request):
    return render(request, "app/splash.html")
