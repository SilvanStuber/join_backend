from rest_framework import serializers
from tasks_app.models import Task, SubTask

"""
Serializer for the SubTask model.

Meta Attributes:
    model: Specifies the SubTask model for serialization.
    fields (list): Defines the fields to include:
        - id: The primary key of the SubTask.
        - description: The description of the SubTask.
        - completed: A boolean indicating whether the SubTask is completed.
"""
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'description', 'completed']

"""
Serializer for the Task model, including nested SubTask objects.

Attributes:
    id (ReadOnlyField): Task ID, read-only.
    sub_tasks (SubTaskSerializer): Nested serializer for associated SubTask objects.

Meta:
    model: Specifies the Task model for serialization.
    fields: Includes all task fields and nested sub_tasks:
        - id, pk, title, task_status, description, assigned, due_date, 
          priority_content, category, sub_tasks.

Methods:
    create(validated_data):
        - Extracts sub_tasks data, creates the Task object, and associates SubTasks.
        - Ensures SubTasks are either created or retrieved if they exist.

    update(instance, validated_data):
        - Updates the Task instance.
        - Updates or creates associated SubTasks, replacing the current ones if provided.
        - Ensures proper linkage of SubTasks to the updated Task.
"""
class TasksSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField() 
    sub_tasks = SubTaskSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = [
            'id', 'pk', 'title', 'task_status', 'description',
            'assigned', 'due_date', 'priority_content',
            'category', 'sub_tasks'
        ]
    def create(self, validated_data):
        sub_tasks_data = validated_data.pop('sub_tasks', [])
        task = Task.objects.create(**validated_data)
        for sub_task_data in sub_tasks_data:
            sub_task_instance, created = SubTask.objects.get_or_create(**sub_task_data)
            task.sub_tasks.add(sub_task_instance)
        return task

    def update(self, instance, validated_data):
        sub_tasks_data = validated_data.pop('sub_tasks', [])
        instance = super().update(instance, validated_data)
        if sub_tasks_data:
            sub_task_instances = []
            for sub_task_data in sub_tasks_data:
                sub_task_instance, created = SubTask.objects.get_or_create(**sub_task_data)
                sub_task_instances.append(sub_task_instance)
            instance.sub_tasks.set(sub_task_instances)
        return instance
