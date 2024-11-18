from django.contrib.auth.models import User 
from django.db import models

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



