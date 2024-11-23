from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from tasks_app.models import Task
from .serializer import TasksSerializer
from django.db.models import Q
"""
A custom viewset combining multiple mixins for handling common CRUD operations.

Inherits:
    mixins.CreateModelMixin: Provides functionality to create objects.
    mixins.ListModelMixin: Provides functionality to list objects.
    mixins.RetrieveModelMixin: Provides functionality to retrieve a single object.
    mixins.UpdateModelMixin: Provides functionality to update objects.
    mixins.DestroyModelMixin: Provides functionality to delete objects.
    viewsets.GenericViewSet: Base class to enable custom behavior in viewsets.

Usage:
    Extend this class to implement viewsets with full CRUD capabilities.
"""
class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    pass

"""
ViewSet for managing Task objects with enhanced filtering and permissions.

Inherits:
    CreateListRetrieveViewSet: Provides full CRUD functionality for tasks.

Attributes:
    serializer_class (TasksSerializer): Specifies the serializer to use for Task objects.
    permission_classes (list): Enforces IsAuthenticated permission.
    queryset (QuerySet): Default queryset for Task objects.

Methods:
    get_queryset():
        - Filters tasks to include only those:
            - Created by the authenticated user (creator).
            - Assigned to the authenticated user (via username in assigned).

    perform_create(serializer):
        - Automatically assigns the authenticated user as the creator of the task when a new task is created.
"""

class TasksViewSets(CreateListRetrieveViewSet):
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all() 

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(
            Q(creator=user) |
            Q(assigned__icontains=user.username) 
        )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

