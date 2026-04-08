""" Admin configuration for Institutions and Departments in the organizational structure.
    This module registers the Institution and Department models with the Django admin site, 
    allowing administrators to manage these entities through the Django admin interface.
"""

from django.contrib import admin
from .models import Institution, Department


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')
    list_filter = ('institution',)
