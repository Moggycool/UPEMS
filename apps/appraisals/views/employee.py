"""employee.py - Views for employee dashboard and related pages."""
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.appraisals.mixins import GroupRequiredMixin, EmployeeProfileRequiredMixin


class EmployeeDashboardView(GroupRequiredMixin, EmployeeProfileRequiredMixin, TemplateView):
    """Dashboard for employees to view their appraisal status and tasks."""
    required_groups = ["EMPLOYEE"]
    template_name = "appraisals/employee/dashboard.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["employee"] = self.employee
        return ctx


# Optional: keep only if you still want /employee/ route during transition
def employee_dashboard(request: HttpRequest) -> HttpResponse:
    """Function-based view wrapper for EmployeeDashboardView."""
    return EmployeeDashboardView.as_view()(request)


def employee_self_behavior_form(request: HttpRequest) -> HttpResponse:
    """View for employees to fill out their self-assessment behavior form."""
    return render(request, "appraisals/employee/self_behavior_form.html")
