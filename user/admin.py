from django.contrib import admin
from user.models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('username', 'nick_name', 'gender', 'phone')
