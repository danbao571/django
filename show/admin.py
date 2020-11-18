from django.contrib import admin
from show.models import News
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'linkman', 'phone', 'address')
