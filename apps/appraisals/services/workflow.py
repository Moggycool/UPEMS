""" Workflow logic for appraisals, including peer assignment and evaluation processes.
    This module contains functions that manage the workflow of performance evaluations, 
    such as assigning peers to evaluations and orchestrating the evaluation process. 
    It interacts with the models to ensure that the necessary relationships are established 
    for accurate scoring and feedback collection.
"""
# apps/appraisals/services/workflow.py
from django.apps import apps


def assign_peers_to_evaluation(evaluation, peer_employees):
    """peer_employees is a list of Employee objects"""
    peer_assignment_model = apps.get_model("appraisals", "PeerAssignment")
    for emp in peer_employees:
        peer_assignment_model.objects.get_or_create(
            evaluation=evaluation, peer=emp)
