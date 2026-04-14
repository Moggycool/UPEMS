""" Admin configuration for organizational structure models. """

from django.contrib import admin
from .models import Employee, ReportingLine, WorkUnit


@admin.register(WorkUnit)
class WorkUnitAdmin(admin.ModelAdmin):
    """ Admin configuration for WorkUnit model."""
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """ Admin configuration for Employee model."""
    list_display = ("employee_no", "full_name", "work_unit", "job_title")
    list_filter = ("work_unit",)
    search_fields = ("employee_no", "full_name", "job_title")


@admin.register(ReportingLine)
class ReportingLineAdmin(admin.ModelAdmin):
    """ Admin configuration for ReportingLine model."""
    list_display = ("employee", "immediate_supervisor", "unit_head", "hr_head")
    search_fields = (
        "employee__full_name",
        "immediate_supervisor__full_name",
        "unit_head__full_name",
        "hr_head__full_name",
    )
