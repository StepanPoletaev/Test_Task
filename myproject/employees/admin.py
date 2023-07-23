from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = 'pk', 'full_name', 'email', 'department', 'leader'
    list_display_links = 'pk', 'full_name'
    ordering = 'pk',
    search_fields = 'full_name', 'department'


@admin.action(description='Activate department')
def mark_activate(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(active=True)


@admin.action(description='Deactivate department')
def mark_deactivate(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(active=False)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    actions = [
        mark_activate,
        mark_deactivate,
    ]
    list_display = 'pk', 'name', 'code', 'leader', 'active'
    list_display_links = 'pk', 'name'
    ordering = 'pk',
    search_fields = 'leader',

