from django.http import HttpRequest, HttpResponse


def index(_request: HttpRequest) -> HttpResponse:
    return HttpResponse("Reports home")
