from django.contrib import admin
from webapp.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Project)