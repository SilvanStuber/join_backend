from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    task_status = models.CharField(max_length=20)
    description = models.TextField()
    assigned = models.ForeignKey('UserContact', on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority_content = models.CharField(max_length=255)
    sub_tasks = models.ManyToManyField('SubTask', blank=True, default="")
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class UserContact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
    
class SubTask(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
