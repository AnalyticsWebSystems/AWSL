from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Technology, Testimonial, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm


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


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    comments = project.comments.all()
    comment_count = comments.count()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment has been posted.')
            return redirect('app:project_detail', project_id=project.id)
    else:
        form = CommentForm()

    return render(request, 'app/project_detail.html', {
        'project': project,
        'comments': comments,
        'form': form,
        'comment_count': comment_count,
    })


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('app:project_detail', project_id=comment.project.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'app:edit_comment.html', {'form': form})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    project_id = comment.project.id
    comment.delete()
    return redirect('app:project_detail', project_id=project_id)


# def project_detail(request, project_id):
#     project = get_object_or_404(Project, pk=project_id)
#     return render(request, 'app/project_detail.html', {'project': project})


def splash(request):
    return render(request, "app/splash.html")
