from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TasksSerializer, ContactSerializer
from tasks_app.models import Task, UserContact
from rest_framework import viewsets
from rest_framework import mixins, viewsets


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



class ContactsViewSets(CreateListRetrieveViewSet):
    queryset = UserContact.objects.all()
    serializer_class = ContactSerializer


    

