""" Scoring logic for appraisals, including the 70/30 split and behavior rating calculations.
    This module implements the core scoring logic for performance evaluations, 
    adhering to the 70/30 split as outlined in Form 16. It calculates the task 
    performance score based on weighted scores and computes the behavior assessment 
    score using ratings from self, peers, and supervisors. 
    The final total score is then saved to the PerformanceEvaluation model.
"""
# apps/appraisals/services/scoring.py


def calculate_evaluation_score(evaluation):
    """
    Calculates the 70/30 split logic based on Form 16.
    """
    # 1. Task Performance (70%)
    tasks = evaluation.tasks.all()
    total_task_weighted = sum(t.weighted_score_e for t in tasks)
    # Scale: (Sum of weighted scores / 100) * 70
    evaluation.task_score_70 = (total_task_weighted * 0.70)

    # 2. Behavior Assessment (30%)
    # Weights: Self(5%), Peer(15%), Supervisor(10%)
    ratings = evaluation.behavior_ratings.all()

    def get_avg_for_role(role_code):
        role_ratings = ratings.filter(role=role_code)
        if not role_ratings.exists():
            return 0
        # Convert 1-4 scale to percentage
        avg = sum(r.rating for r in role_ratings) / role_ratings.count()
        return (avg / 4.0)

    self_contribution = get_avg_for_role('SELF') * 5
    peer_contribution = get_avg_for_role('PEER') * 15
    sup_contribution = get_avg_for_role('SUPERVISOR') * 10

    evaluation.behavior_score_30 = self_contribution + \
        peer_contribution + sup_contribution
    evaluation.total_score = evaluation.task_score_70 + evaluation.behavior_score_30
    evaluation.save()
