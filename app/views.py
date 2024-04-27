from django.shortcuts import render
from .models import Project, Technology, Testimonial


# Create your views here.
def index(request):
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    project_count = projects.count()
    technologies = Technology.objects.all()

    return render(request, "app/index.html", {
        "projects": projects,
        "technologies": technologies,
        "project_count": project_count,
        "testimonials": testimonials,
    })


def splash(request):
    return render(request, "app/splash.html")
