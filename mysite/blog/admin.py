from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    https://runebook.dev/ru/docs/django/ref/contrib/admin/index#django.contrib.admin.ModelAdmin.list_filter
    """
    list_display = ['title', 'author', 'created', 'updated', 'status']
    list_filter = ('status', 'created', 'publish',)
    search_fields = ("title", 'body',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    odrering = ['status', 'publish']


admin.site.register(Post, PostAdmin)
