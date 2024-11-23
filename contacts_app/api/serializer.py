from rest_framework import serializers
from contacts_app.models import UserContact

"""
Serializer for UserContact model.

Attributes:
    pk (ReadOnlyField): Primary key of the contact, read-only.
    user (ReadOnlyField): Username of the associated user, read-only.

Meta:
    model: Specifies the UserContact model for serialization.
    fields: Includes all fields from the UserContact model.
"""
class ContactSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserContact
        fields = '__all__'
