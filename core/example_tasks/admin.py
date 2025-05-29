from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_completed', 'priority', 'created_at')
    list_filter = ('is_completed', 'priority')
    search_fields = ('name',)
    list_editable = ('is_completed', 'priority')
