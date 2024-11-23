from rest_framework import serializers
from tasks_app.models import Task, SubTask

"""
Serializer for the SubTask model.

Meta:
    model (Model): Specifies the SubTask model to be serialized.
    fields (list): Defines the fields to include in the serialized output:
        - id: The primary key of the sub-task.
        - description: A brief description of the sub-task.
        - completed: A boolean indicating whether the sub-task is completed.
"""
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'description', 'completed']

"""
Serializer for the Task model with nested SubTask objects.

Attributes:
    id (ReadOnlyField): Task ID, read-only.
    sub_tasks (SubTaskSerializer): Serializer for associated SubTask objects (optional, many).

Meta:
    model (Model): Specifies the Task model to be serialized.
    fields (list): Includes all relevant fields for a Task:
        - id, pk, title, task_status, description, assigned, due_date,
          priority_content, category, and sub_tasks.

Methods:
    create(validated_data):
        - Handles the creation of a Task object along with its nested SubTasks.
        - SubTasks are created or retrieved and associated with the Task.

    update(instance, validated_data):
        - Updates a Task object and its nested SubTasks.
        - Ensures SubTasks are created or updated and replaces existing associations.
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
