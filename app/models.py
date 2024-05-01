from django.db import models
from userauths.models import User


class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)

    # technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    client = models.CharField(max_length=100)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    team = models.ManyToManyField('TeamMember', related_name='projects')
    technologies_used = models.ManyToManyField('Technology', related_name='projects')
    image = models.ImageField(upload_to='project_images')
    more_images1 = models.ImageField(upload_to='project_images', null=True, blank=True)
    more_images2 = models.ImageField(upload_to='project_images', null=True, blank=True)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='team_images')

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
