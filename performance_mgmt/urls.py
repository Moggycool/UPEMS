"""URL configuration for performance_mgmt project."""
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include, path


urlpatterns = [
    path("", RedirectView.as_view(url="/accounts/", permanent=False)),
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("appraisals/", include("apps.appraisals.urls")),
    path("reports/", include("apps.reports.urls")),
]
