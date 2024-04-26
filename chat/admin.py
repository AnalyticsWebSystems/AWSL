from django.contrib import admin

# Register your models here.
from .models import Message, Representative, Conversation

admin.site.register(Message)
admin.site.register(Representative)
admin.site.register(Conversation)
