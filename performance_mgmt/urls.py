"""URL configuration for performance_mgmt project."""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/my/", permanent=False)),
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),

    # keep only this one
    path("", include("apps.appraisals.urls")),

    path("reports/", include("apps.reports.urls")),
]
