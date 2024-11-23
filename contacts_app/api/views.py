from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from contacts_app.models import UserContact
from .serializer import ContactSerializer
from rest_framework.permissions import BasePermission

"""
A custom viewset combining common mixins for CRUD operations.

Inherits:
    mixins.CreateModelMixin: Provides create functionality.
    mixins.ListModelMixin: Provides list functionality.
    mixins.RetrieveModelMixin: Provides retrieve functionality.
    mixins.UpdateModelMixin: Provides update functionality.
    mixins.DestroyModelMixin: Provides delete functionality.
    viewsets.GenericViewSet: Base viewset for combining mixins.

Usage:
    Extend this class to create a viewset with full CRUD capabilities.
"""
class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    pass

"""
Custom permission to ensure the requesting user owns the object.

Methods:
    has_object_permission(request, view, obj):
        - Checks if the object's `user` attribute matches the authenticated user.

Returns:
    bool: True if the object belongs to the requesting user, False otherwise.
"""
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
"""
Viewset for managing UserContact objects.

Inherits:
    CreateListRetrieveViewSet: Provides create, list, retrieve, update, and delete functionality.

Attributes:
    serializer_class (Serializer): Specifies the serializer for UserContact.
    permission_classes (list): Enforces IsAuthenticated and IsOwner permissions.

Methods:
    get_queryset():
        - Filters UserContact objects to include only those owned by the authenticated user.
    perform_create(serializer):
        - Automatically assigns the authenticated user as the owner when creating a new contact.
"""
class ContactsViewSets(CreateListRetrieveViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return UserContact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


