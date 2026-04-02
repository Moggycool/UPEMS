from django.http import HttpRequest, HttpResponse


def dashboard(_request: HttpRequest) -> HttpResponse:
    return HttpResponse("Accounts dashboard")
