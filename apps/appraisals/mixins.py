""" mixins.py - Common mixins for appraisal views, e.g. RBAC and profile checks. """
from typing import TYPE_CHECKING, Any, Protocol, cast

from django.http import HttpRequest
from django.http.response import HttpResponseBase
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

if TYPE_CHECKING:
    from apps.org.models import Employee


class _DispatchProtocol(Protocol):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        ...


class _UserWithEmployee(Protocol):
    employee: "Employee"


class GroupRequiredMixin(LoginRequiredMixin):
    """
    Strict RBAC (Option 1):
    - User must be authenticated
    - AND must belong to at least one group in `required_groups`
    - superuser bypasses
    """
    required_groups: list[str] = []

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        if request.user.is_superuser:
            return cast(_DispatchProtocol, super()).dispatch(request, *args, **kwargs)

        if not self.required_groups:
            raise RuntimeError(
                f"{self.__class__.__name__} must define required_groups = ['EMPLOYEE', ...]"
            )

        user_group_names = set(
            request.user.groups.values_list("name", flat=True))
        if not user_group_names.intersection(set(self.required_groups)):
            raise PermissionDenied(
                "You do not have permission to access this page.")

        return cast(_DispatchProtocol, super()).dispatch(request, *args, **kwargs)


class EmployeeProfileRequiredMixin:
    """
    Ensures the logged-in user has an Employee profile at request.user.employee.
    Depends on org.Employee(user=OneToOneField(User, related_name='employee')).
    """

    employee: "Employee"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        """ Check for Employee profile. """
        # If user is not authenticated, LoginRequiredMixin should handle it,
        # but guard anyway so we don't raise confusing errors.
        if not request.user.is_authenticated:
            return cast(_DispatchProtocol, super()).dispatch(request, *args, **kwargs)

        if not hasattr(request.user, "employee"):
            raise PermissionDenied(
                "Employee profile not configured for this account.")

        self.employee = cast(_UserWithEmployee, request.user).employee

        return cast(_DispatchProtocol, super()).dispatch(request, *args, **kwargs)
