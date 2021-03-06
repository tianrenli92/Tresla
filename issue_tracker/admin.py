from django.contrib import admin
from .models import Issue, Project, Comment


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Issue)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'approved')


admin.site.register(Comment)

# Register your models here.
