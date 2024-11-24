from django.db import models
from django.contrib.auth.models import User

"""
Model for representing tasks with detailed attributes and relationships.

Attributes:
    title (CharField): Title of the task (max length 255).
    task_status (CharField): Status of the task (e.g., "todo", "inProgress").
    description (TextField): Detailed description of the task.
    assigned (JSONField): List of assigned usernames.
    due_date (DateField): Due date for the task; defaults to '1999-01-01'.
    priority_content (CharField): Priority level of the task (e.g., "urgent").
    category (JSONField): List of task categories.
    creator (ForeignKey): User who created the task.
    sub_tasks (ManyToManyField): Related SubTask objects.

Methods:
    add_to_assigned(name):
        - Adds a name to the assigned list and saves the task.
    add_to_category(category_name):
        - Adds a category name to the category list and saves the task.
    add_to_sub_tasks(sub_task):
        - Adds a SubTask instance to the task's sub_tasks and saves it.

Returns:
    str: Title of the task as its string representation.
"""
class Task(models.Model):
    title = models.CharField(max_length=255, default="")
    task_status = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    assigned = models.JSONField(default=list, blank=True)
    due_date = models.DateField(null=True, blank=True, default='1999-01-01')
    priority_content = models.CharField(max_length=255, default="")
    category = models.JSONField(default=list)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tasks")
    sub_tasks = models.ManyToManyField('SubTask', related_name='tasks', blank=True)

    def add_to_assigned(self, name):
        if isinstance(self.assigned, list): 
            self.assigned.append(name)
            self.save()

    def add_to_category(self, category_name):
        if isinstance(self.category, list):
            self.category.append(category_name)
            self.save()

    def add_to_sub_tasks(self, sub_task):
        if isinstance(sub_task, SubTask):
            self.sub_tasks.add(sub_task)
            self.save()

    def __str__(self):
        return self.title

"""
Model for storing user contact information.

Attributes:
    name (CharField): Name of the contact (max length 255).
    email (CharField): Email address of the contact (max length 255).
    phone (CharField): Phone number of the contact (max length 15).

Methods:
    __str__():
        - Returns the contact's name as the string representation.
"""
class UserContact(models.Model):
    name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name

"""
Model for representing a sub-task associated with a Task.

Attributes:
    description (CharField): Brief description of the sub-task (max length 255).
    completed (BooleanField): Indicates whether the sub-task is completed (default: False).

Methods:
    __str__():
        - Returns the description of the sub-task as its string representation.
"""
class SubTask(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

