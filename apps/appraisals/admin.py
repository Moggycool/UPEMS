""" admin.py - Admin site configuration for appraisals app. """
from django.contrib import admin

from apps.appraisals.models import (
    EvaluationCycle,
    Evaluation,
    BehavioralAttribute,
    BehavioralSubmission,
    BehavioralScore,
    PeerAssignment,
)

admin.site.register(EvaluationCycle)
admin.site.register(Evaluation)
admin.site.register(BehavioralAttribute)
admin.site.register(BehavioralSubmission)
admin.site.register(BehavioralScore)
admin.site.register(PeerAssignment)
