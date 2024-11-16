from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from contacts_app.models import UserContact
from .serializer import ContactSerializer

class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    pass

class ContactsViewSets(CreateListRetrieveViewSet):
    queryset = UserContact.objects.all()
    serializer_class = ContactSerializer

