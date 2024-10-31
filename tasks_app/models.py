from django.db import models


class task(models.Model):
    title = models.CharField(max_length=255)
    taskStatus = models.CharField(max_length=255)
    description = models.TextField(max_length=255)  # add_task1 save()
    assigned = models.CharField(max_length=255)
    dueDate = models.CharField(max_length=255)
    priorityContentArray = models.CharField(max_length=255)
    subtasks = models.CharField(max_length=255)
    tasks = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subT = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class contact(models.Model):
    title = models.CharField(max_length=255)
    taskStatus = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title
