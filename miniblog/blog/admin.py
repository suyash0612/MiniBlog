from django.contrib import admin
from .models import PostModel


# Register your models here.
@admin.register(PostModel)
class PostAdminModel(admin.ModelAdmin):
    list_display = ['title','desc']

