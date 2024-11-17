from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from tasks_app.models import Task
from .serializer import TasksSerializer
from django.db.models import Q

class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    pass

class TasksViewSets(CreateListRetrieveViewSet):
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()  # Dummy-Wert, wird durch `get_queryset` überschrieben

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(
            Q(creator=user) |
            Q(assigned__icontains=user.username)  # icontains prüft auf den String innerhalb des JSON-Felds
        )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

