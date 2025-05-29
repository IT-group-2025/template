from django.contrib import admin
from .models import Employee, Project, Assignment

class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1
    fields = ('employee', 'role', 'assigned_date')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'get_projects')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [AssignmentInline]

    def get_projects(self, obj):
        return ", ".join([project.name for project in obj.projects.all()])
    get_projects.short_description = 'Проекты'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'get_employees')
    list_filter = ('start_date',)
    search_fields = ('name', 'description')
    inlines = [AssignmentInline]

    def get_employees(self, obj):
        return ", ".join([f"{assignment.employee} ({assignment.role})" for assignment in obj.assignment_set.all()])
    get_employees.short_description = 'Сотрудники'

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project', 'role', 'assigned_date')
    list_filter = ('role', 'assigned_date')
    search_fields = ('employee__first_name', 'employee__last_name', 'project__name')

