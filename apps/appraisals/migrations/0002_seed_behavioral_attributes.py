from django.db import migrations


def seed_behavioral_attributes(apps, schema_editor):
    BehavioralAttribute = apps.get_model("appraisals", "BehavioralAttribute")

    data = [
        ("aaa", 25),
        ("bbb", 20),
        ("ccc", 15),
        ("fff", 15),
        ("ggg", 15),
        ("hhh", 10),
    ]

    for name, weight in data:
        BehavioralAttribute.objects.update_or_create(
            name=name,
            defaults={"weight": weight, "is_active": True},
        )


def unseed_behavioral_attributes(apps, schema_editor):
    BehavioralAttribute = apps.get_model("appraisals", "BehavioralAttribute")
    names = ["aaa", "bbb", "ccc", "fff", "ggg", "hhh"]
    BehavioralAttribute.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("appraisals", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_behavioral_attributes,
                             unseed_behavioral_attributes),
    ]
