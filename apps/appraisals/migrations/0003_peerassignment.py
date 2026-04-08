import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("org", "0001_initial"),
        ("appraisals", "0002_seed_behavioral_attributes"),
    ]

    operations = [
        migrations.CreateModel(
            name="PeerAssignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(
                    default=django.utils.timezone.now)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="peer_assignments",
                        to="appraisals.evaluation",
                    ),
                ),
                (
                    "peer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="peer_assignments",
                        to="org.employee",
                    ),
                ),
            ],
            options={
                "constraints": [
                    models.UniqueConstraint(
                        fields=("evaluation", "peer"), name="uniq_peer_assignment"
                    ),
                ],
            },
        ),
    ]
