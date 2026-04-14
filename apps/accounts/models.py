"""Models for the accounts app, defining the Employee model which extends the built-in 
   User model with additional fields such as department. 
   This allows for a more comprehensive representation of employees within the system, 
   linking them to their respective departments and enabling integration with other modules 
   like performance evaluations and organizational structure.
"""
from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    """Employee model linked to Django's User, with organizational details."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(
        'org.Department', on_delete=models.SET_NULL, null=True)
    # ...
