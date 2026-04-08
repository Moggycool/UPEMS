""" models.py - DB models for appraisals app. """
from django.db import models
from django.utils import timezone

from apps.org.models import Employee


class EvaluationCycle(models.Model):
    """
    One row per cycle, e.g. 2026-H1 or 2026-H2.
    """
    H1 = "H1"
    H2 = "H2"
    HALF_CHOICES = [(H1, "H1"), (H2, "H2")]

    year = models.PositiveIntegerField()
    half = models.CharField(max_length=2, choices=HALF_CHOICES)

    start_date = models.DateField()
    end_date = models.DateField()

    is_active = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["year", "half"], name="uniq_cycle_year_half"),
        ]

    def __str__(self) -> str:
        return f"{self.year}-{self.half}"


class Evaluation(models.Model):
    """
    The evaluation record for one employee in one cycle.
    """
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    APPROVED = "APPROVED"
    REOPENED = "REOPENED"

    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (SUBMITTED, "Submitted"),
        (UNDER_REVIEW, "Under review"),
        (APPROVED, "Approved"),
        (REOPENED, "Reopened"),
    ]

    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name="evaluations")
    cycle = models.ForeignKey(
        EvaluationCycle, on_delete=models.PROTECT, related_name="evaluations")

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=DRAFT)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "cycle"], name="uniq_eval_employee_cycle"),
        ]

    def __str__(self) -> str:
        return f"Evaluation({self.employee} / {self.cycle})"


class BehavioralAttribute(models.Model):
    """
    Seeded list of behavioral attributes and their weights (sum = 100).
    """
    name = models.CharField(max_length=200, unique=True)
    weight = models.PositiveIntegerField()  # 0..100

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.name} ({self.weight}%)"


class BehavioralSubmission(models.Model):
    """
    One submission per evaluation per role (self, peer, supervisor).
    """
    ROLE_SELF = "SELF"
    ROLE_PEER = "PEER"
    ROLE_SUPERVISOR = "SUPERVISOR"

    ROLE_CHOICES = [
        (ROLE_SELF, "Self"),
        (ROLE_PEER, "Peer"),
        (ROLE_SUPERVISOR, "Supervisor"),
    ]

    evaluation = models.ForeignKey(
        Evaluation, on_delete=models.CASCADE, related_name="behavioral_submissions")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    submitted_by = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name="behavioral_submissions_made")

    is_submitted = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["evaluation", "role", "submitted_by"], name="uniq_submission"),
        ]

    def __str__(self) -> str:
        return f"BehavioralSubmission({self.evaluation} / {self.role} / {self.submitted_by})"


class BehavioralScore(models.Model):
    """
    Score per attribute for a given submission.
    """
    submission = models.ForeignKey(
        BehavioralSubmission, on_delete=models.CASCADE, related_name="scores")
    attribute = models.ForeignKey(
        BehavioralAttribute, on_delete=models.PROTECT, related_name="scores")

    # Score 1..5 (you can enforce in forms; DB constraint optional later)
    score = models.PositiveSmallIntegerField()

    comment = models.TextField(blank=True, default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["submission", "attribute"], name="uniq_submission_attribute"),
        ]

    def __str__(self) -> str:
        return f"{self.submission} / {self.attribute} = {self.score}"


class PeerAssignment(models.Model):
    """
    Assigns a peer reviewer to an evaluation.
    """
    evaluation = models.ForeignKey(
        Evaluation, on_delete=models.CASCADE, related_name="peer_assignments"
    )
    peer = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name="peer_assignments"
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["evaluation", "peer"], name="uniq_peer_assignment"
            ),
        ]

    def __str__(self) -> str:
        return f"PeerAssignment({self.evaluation} / {self.peer})"
