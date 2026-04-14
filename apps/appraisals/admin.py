""" Admin configuration for the Performance Evaluation system, allowing HR to manage evaluations,
    tasks, behavior ratings, and peer assignments.
    This module defines the admin interface for the appraisal system, enabling HR personnel 
    to view and manage performance evaluations, including the associated tasks, behavior ratings, 
    and peer assignments. The admin configuration includes custom list displays, filters, 
    and inlines to facilitate efficient management of evaluations and related data, 
    ensuring that HR can easily access and update the necessary information 
    for each employee's performance evaluation process.
"""
from django.contrib import admin
# Use explicit relative imports to avoid "unknown symbol" errors
from .models import PerformanceEvaluation, TaskItem, BehaviorRating, PeerAssignment


class TaskItemInline(admin.TabularInline):
    """Inline for editing individual tasks within an evaluation."""
    model = TaskItem
    extra = 1
    fields = ('description', 'weight_a', 'goal_b', 'actual_c')


class BehaviorRatingInline(admin.TabularInline):
    """Inline for viewing/editing behavior scores (Self/Peer/Supervisor)."""
    model = BehaviorRating
    extra = 0
    # Usually HR shouldn't change raw ratings, but we allow it here for Admin
    fields = ('rater', 'role', 'attribute_name', 'rating')


class PeerAssignmentInline(admin.TabularInline):
    """Inline for managing who is assigned to evaluate this employee."""
    model = PeerAssignment
    extra = 0
    readonly_fields = ('is_completed',)


@admin.register(PerformanceEvaluation)
class PerformanceEvaluationAdmin(admin.ModelAdmin):
    """Main Command Center for HR to view and manage Employee Evaluations."""

    # 1. Table View Configuration
    list_display = (
        'employee',
        'period',
        'display_task_70',
        'display_behavior_30',
        'total_score',
        'status'
    )
    list_filter = ('status', 'period', 'employee__work_unit')
    search_fields = ('employee__user__first_name', 'employee__user__last_name')

    # 2. Detail Page Configuration (Grouping fields and adding Inlines)
    inlines = [TaskItemInline, BehaviorRatingInline, PeerAssignmentInline]

    fieldsets = (
        ('Reference Information', {
            'fields': ('employee', 'period', 'status')
        }),
        ('Mathematical Summary (Read-Only)', {
            'fields': ('task_score_70', 'behavior_score_30', 'total_score'),
            'description': "These scores are updated via the system's scoring service."
        }),
    )

    readonly_fields = ('task_score_70', 'behavior_score_30', 'total_score')

    # 3. Custom Formatting for Display
    def display_task_70(self, obj):
        """Show task score with 2 decimals in the list view."""
        return f"{obj.task_score_70:.2f}"
    display_task_70.short_description = 'Task (70%)'

    def display_behavior_30(self, obj):
        """Show behavior score with 2 decimals in the list view."""
        return f"{obj.behavior_score_30:.2f}"
    display_behavior_30.short_description = 'Behavior (30%)'

# Also register BehaviorRating standalone just in case HR needs to search specific ratings


@admin.register(BehaviorRating)
class BehaviorRatingAdmin(admin.ModelAdmin):
    """Admin configuration for BehaviorRating model, allowing HR to search 
    and filter behavior ratings.
    This admin configuration provides HR personnel with the ability to search and filter
    behavior ratings based on various criteria, such as the employee being evaluated, 
    the rater, and the specific behavioral attribute. It includes custom list displays and 
    search fields to facilitate efficient management of behavior ratings, 
    ensuring that HR can easily access and update the necessary information for each rating 
    as part of the overall performance evaluation process.
    """
    list_display = ('evaluation', 'rater', 'role', 'rating')
    list_filter = ('role', 'rating')
    search_fields = (
        'evaluation__employee__user__first_name',
        'evaluation__employee__user__last_name',
        'rater__user__first_name',
        'rater__user__last_name',
        'attribute_name'
    )
