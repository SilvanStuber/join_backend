from rest_framework import serializers
from contacts_app.models import UserContact

class ContactSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserContact
        fields = '__all__'
