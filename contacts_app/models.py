from django.db import models

class UserContact(models.Model):
    name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name
