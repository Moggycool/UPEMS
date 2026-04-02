from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def employee_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/employee/dashboard.html")


def employee_self_behavior_form(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/employee/self_behavior_form.html")
