"""URL configuration for performance_mgmt project."""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("appraisals/", include("apps.appraisals.urls")),
    path("reports/", include("apps.reports.urls")),
]
