"""Models for the Performance Evaluation system, defining the structure of evaluations, 
   tasks, behavior ratings, and peer assignments.  
   This module contains the core data models for the appraisal system, 
   including PerformanceEvaluation, 
   TaskItem, BehaviorRating, and PeerAssignment. 
   Each model is designed to capture specific aspects of the evaluation process, 
   such as employee details, evaluation periods, task descriptions and weights, 
   behavior attributes, and peer relationships.
"""
from django.db import models


class PerformanceEvaluation(models.Model):
    """Model representing a performance evaluation for an employee, including details about 
       the employee, evaluation period, status, and calculated scores based on tasks 
       and behavior ratings.
       This model captures the essential information for a performance evaluation, 
       linking it to an employee and defining the evaluation period and status.
       It also includes fields for storing the calculated scores for tasks and behavior, 
       as well as the total score, which are updated based on the associated TaskItem and 
       BehaviorRating models.
    """
    STATUS_CHOICES = [('DRAFT', 'Draft'), ('REVIEW',
                                           'Review'), ('FINAL', 'Final')]
    employee = models.ForeignKey('org.Employee', on_delete=models.CASCADE)
    period = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='DRAFT')

    task_score_70 = models.FloatField(default=0.0)
    behavior_score_30 = models.FloatField(default=0.0)
    total_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.employee} - {self.period}"


class TaskItem(models.Model):
    """Model representing a specific task within a performance evaluation, 
       including its description, weight, goal, and actual performance.
       This model is linked to a PerformanceEvaluation and captures the details of 
       individual tasks that contribute to the overall evaluation score. 
       Each task has a description, a weight that indicates its importance in the evaluation, 
       a goal value that represents the target performance, and an actual value that represents 
       the employee's performance on that task. 
       The weighted score for each task can be calculated based on the actual performance 
       relative to the goal, multiplied by the weight.
    """
    evaluation = models.ForeignKey(
        PerformanceEvaluation, related_name='tasks', on_delete=models.CASCADE)
    description = models.TextField()
    weight_a = models.FloatField()
    goal_b = models.FloatField()
    actual_c = models.FloatField()

    @property
    def weighted_score_e(self):
        """Calculate the weighted score for this task based on the actual performance 
           relative to the goal, multiplied by the weight. 
           This property allows for easy retrieval of the weighted score 
           without needing to store it in the database, ensuring that it is always up-to-date 
           with the current values of actual performance and goal.
        """
        if self.goal_b > 0:
            return (self.actual_c / self.goal_b) * self.weight_a
        return 0


class BehaviorRating(models.Model):
    """Model representing a behavior rating for an employee within a performance evaluation, 
       including the rater, role, attribute name, and rating value.
       This model captures the ratings for various behavioral attributes that contribute to 
       the overall evaluation score. Each rating is linked to a specific PerformanceEvaluation 
       and includes information about who provided the rating (rater), their role in the 
       evaluation process (self, peer, or supervisor), the name of the behavioral attribute being 
       rated, and the rating value itself. This allows for a comprehensive assessment of an 
       employee's behavior in addition to their task performance.
    """
    ROLE_CHOICES = [('SELF', 'Self'), ('PEER', 'Peer'),
                    ('SUPERVISOR', 'Supervisor')]
    evaluation = models.ForeignKey(
        PerformanceEvaluation, related_name='behavior_ratings', on_delete=models.CASCADE)
    rater = models.ForeignKey('org.Employee', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    attribute_name = models.CharField(max_length=255)  # e.g., "Punctuality"
    rating = models.IntegerField()  # 1 to 4 scale


class PeerAssignment(models.Model):
    """Model representing the assignment of a peer to a performance evaluation, 
       including the evaluation, peer, and completion status.
       This model captures the relationship between a performance evaluation and the peers 
       assigned to provide feedback or ratings for that evaluation. Each PeerAssignment links 
       a specific PerformanceEvaluation to an Employee who is acting as a peer rater. 
       The model also includes a boolean field to indicate whether the peer has completed their 
       assigned tasks or ratings, allowing for tracking of the evaluation process and ensuring 
       that all necessary feedback is collected before finalizing the evaluation.
    """
    evaluation = models.ForeignKey(
        PerformanceEvaluation, related_name='assigned_peers', on_delete=models.CASCADE)
    peer = models.ForeignKey('org.Employee', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
