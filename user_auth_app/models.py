from django.contrib.auth.models import User
from django.db import models

"""
Model for storing additional profile information for a user.

Attributes:
    user (OneToOneField): Links the profile to a specific User object.
    email (TextField): Email address of the user (optional, can be blank or null).
    phone (CharField): Phone number of the user (optional, max length 100, can be blank or null).

Methods:
    __str__():
        - Returns the username of the associated user as the string representation.
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
