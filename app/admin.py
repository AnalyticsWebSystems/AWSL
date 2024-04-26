from django.contrib import admin
from .models import Technology, TeamMember, Project, Service

# Register your models here.
admin.site.register(Technology)
admin.site.register(TeamMember)
admin.site.register(Project)
admin.site.register(Service)
