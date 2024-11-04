from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, default="")
    task_status = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    assigned = models.JSONField(default=list) 
    due_date = models.DateField(null=True, blank=True, default='1.1.1999')
    priority_content = models.CharField(max_length=255, default="")
    sub_tasks = models.JSONField(default=list)
    category = models.JSONField(default=list) 

    def add_to_assigned(self, name):
        if isinstance(self.assigned, list): 
            self.assigned.append(name)
            self.save()
    
    def add_to_sub_tasks(self, title):
        if isinstance(self.sub_tasks, list): 
            self.sub_tasks.append(title)
            self.save()
    
    def add_to_category(self, category_name):
        if isinstance(self.category, list):
            self.category.append(category_name)
            self.save()

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
