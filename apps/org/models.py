""" Models for organizational structure: work units, employees, and reporting lines.
"""
from django.conf import settings
from django.db import models


class WorkUnit(models.Model):
    """ Represents a work unit or department within the organization. """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return str(self.name)


class Employee(models.Model):
    """ Represents an employee within the organization. """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="employee"
    )

    employee_no = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=200)

    work_unit = models.ForeignKey(
        WorkUnit, on_delete=models.PROTECT, related_name="employees", null=True, blank=True
    )

    job_title = models.CharField(max_length=200, blank=True, default="")

    def __str__(self) -> str:
        return f"{self.full_name} ({self.employee_no})"


class ReportingLine(models.Model):
    """ Represents the reporting line for an employee.
        One row per employee that defines:
        employee -> immediate supervisor -> unit head -> HR head
    """

    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="reporting_line"
    )

    immediate_supervisor = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name="direct_reports", null=True, blank=True
    )
    unit_head = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name="unit_head_reports", null=True, blank=True
    )
    hr_head = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name="hr_head_reports", null=True, blank=True
    )

    def __str__(self) -> str:
        return f"ReportingLine(employee={self.employee})"
