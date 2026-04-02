""" ASGI config for performance_mgmt project."""
import os

from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "performance_mgmt.settings")

application = get_asgi_application()
