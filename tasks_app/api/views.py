from rest_framework import mixins, viewsets
from tasks_app.models import Task, UserContact
from .serializer import TasksSerializer

class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    pass

class TasksViewSets(CreateListRetrieveViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

