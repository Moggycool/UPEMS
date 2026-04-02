from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def unit_head_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/unit_head/dashboard.html")


def unit_head_review(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/unit_head/review.html")
