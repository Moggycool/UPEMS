"""Views for supervisor-related appraisal pages."""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def supervisor_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/supervisor/dashboard.html")


def supervisor_review(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/supervisor/review.html")


def supervisor_select_peers(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/supervisor/select_peers.html")


def supervisor_tasks_form(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/supervisor/tasks_form.html")


def supervisor_behavior_form(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/supervisor/supervisor_behavior_form.html")
