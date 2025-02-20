from django.contrib import admin
from .models import Project, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1  # Nombre de tâches vides à afficher

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'description')
    inlines = [TaskInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task)