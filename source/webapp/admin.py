from django.contrib import admin
from webapp.models import Project, News

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Project)
admin.site.register(News)