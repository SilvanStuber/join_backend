from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from contacts_app.models import UserContact
from .serializer import ContactSerializer
from rest_framework.permissions import BasePermission

class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    pass

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class ContactsViewSets(CreateListRetrieveViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return UserContact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


