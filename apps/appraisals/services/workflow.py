""" Workflow logic for appraisals, including peer assignment and evaluation processes.
    This module contains functions that manage the workflow of performance evaluations, 
    such as assigning peers to evaluations and orchestrating the evaluation process. 
    It interacts with the models to ensure that the necessary relationships are established 
    for accurate scoring and feedback collection.
"""
# apps/appraisals/services/workflow.py
from ..models import PeerAssignment


def assign_peers_to_evaluation(evaluation, peer_employees):
    """peer_employees is a list of Employee objects"""
    for emp in peer_employees:
        PeerAssignment.objects.get_or_create(evaluation=evaluation, peer=emp)
