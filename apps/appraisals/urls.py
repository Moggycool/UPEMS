from django.urls import path

from .views import (
    employee_dashboard,
    employee_self_behavior_form,
    hr_dashboard,
    hr_reopen_form,
    hr_review,
    peer_behavior_form,
    peer_dashboard,
    supervisor_behavior_form,
    supervisor_dashboard,
    supervisor_review,
    supervisor_select_peers,
    supervisor_tasks_form,
    unit_head_dashboard,
    unit_head_review,
)


app_name = "appraisals"

urlpatterns = [
    path("employee/", employee_dashboard, name="employee-dashboard"),
    path("employee/self-behavior/", employee_self_behavior_form,
         name="employee-self-behavior"),
    path("hr/", hr_dashboard, name="hr-dashboard"),
    path("hr/review/", hr_review, name="hr-review"),
    path("hr/reopen/", hr_reopen_form, name="hr-reopen"),
    path("peer/", peer_dashboard, name="peer-dashboard"),
    path("peer/behavior/", peer_behavior_form, name="peer-behavior"),
    path("supervisor/", supervisor_dashboard, name="supervisor-dashboard"),
    path("supervisor/review/", supervisor_review, name="supervisor-review"),
    path("supervisor/select-peers/", supervisor_select_peers,
         name="supervisor-select-peers"),
    path("supervisor/tasks/", supervisor_tasks_form, name="supervisor-tasks"),
    path("supervisor/behavior/", supervisor_behavior_form,
         name="supervisor-behavior"),
    path("unit-head/", unit_head_dashboard, name="unit-head-dashboard"),
    path("unit-head/review/", unit_head_review, name="unit-head-review"),
]
