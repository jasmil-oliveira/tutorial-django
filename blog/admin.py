from django.contrib import admin

from .models import Post

@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title","slug","author","created","updated","status","publish")
    prepopulated_fields = {"slug":("title",)}
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['-publish', 'status']