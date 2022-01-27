from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Magazine, Post, Comment


class MagazineAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'intro_text',
        'article',
        'image',
        'date_added',
        'author'
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'comment_text',
        'date_created',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Comment, CommentAdmin)