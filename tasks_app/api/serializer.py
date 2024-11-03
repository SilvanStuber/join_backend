from rest_framework import serializers
from tasks_app.models import Task, UserContact

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        fields = '__all__'

class AssignedContactSerializer(ContactSerializer, serializers.ModelSerializer):
    class Meta:
        model = UserContact
        exclude = ['email']


