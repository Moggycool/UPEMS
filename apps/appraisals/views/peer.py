from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def peer_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/peer/dashboard.html")


def peer_behavior_form(request: HttpRequest) -> HttpResponse:
    return render(request, "appraisals/peer/behavior_form.html")
