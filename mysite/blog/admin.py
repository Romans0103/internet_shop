from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'updated', 'status']


admin.site.register(Post, PostAdmin)
