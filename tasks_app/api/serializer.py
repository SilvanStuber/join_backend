from rest_framework import serializers
from tasks_app.models import Task, SubTask, UserContact

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'description', 'completed']

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

class ContactSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField() 
    class Meta:
        model = UserContact
        fields = '__all__'