from django.contrib.auth.models import User 
from django.db import models


"""
Model for storing user contacts.

Attributes:
    user (ForeignKey): Reference to the associated User object.
    name (CharField): Contact's name (max length 255).
    email (CharField): Contact's email address (max length 255).
    phone (CharField): Contact's phone number (max length 30).

Methods:
    __str__(): Returns the contact's name as string representation.
"""
class UserContact(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="contacts",
    )
    name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name



