from django.contrib import admin
from posts.models import Author, Category, Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user']

admin.site.register(Author, AuthorAdmin)

admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "published_date", "short_description"]

admin.site.register(Post, PostAdmin)