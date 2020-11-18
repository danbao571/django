from django.contrib import admin
from blog.models import Blog, BlogType
# Register your models here.


@admin.register(Blog)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'author')


@admin.register(BlogType)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
