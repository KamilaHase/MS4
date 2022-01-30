from django.contrib import admin

from django.contrib import admin
from .models import Magazine, Post, Comment

""" Renders Models to the Admin View"""


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
        'nickname',
        'comment_text',
        'date_created',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Comment, CommentAdmin)
