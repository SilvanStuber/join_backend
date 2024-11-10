from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, default="")
    task_status = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    assigned = models.JSONField(default=list)
    due_date = models.DateField(null=True, blank=True, default='1999-01-01')  # ISO-Format
    priority_content = models.CharField(max_length=255, default="")
    category = models.JSONField(default=list)
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


class UserContact(models.Model):
    name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name


class SubTask(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class UserContact(models.Model):
    name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name