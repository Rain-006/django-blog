from django.contrib import admin
from .models import Post
from django.db import models
from django.contrib.auth.admin import UserAdmin


admin.site.register(Post)   
class GroupIsAdminClass(UserAdmin):
    list_display = ["title", "content", "created_at"]
