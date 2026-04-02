from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hr_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/hr/dashboard.html")


def hr_review(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/hr/review.html")


def hr_reopen_form(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/hr/reopen_form.html")
