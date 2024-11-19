from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = User
        fields = ['user', 'email', 'phone']

class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']

        if pw != repeated_pw:
            raise serializers.ValidationError({'error': 'passwords dount match'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(pw)
        account.save()
        return account



class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            raise serializers.ValidationError("E-mail and password are required.")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid e-mail address or password.")
        user = authenticate(username=user.username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid e-mail address or password.")
        data['user'] = user
        return data
    
class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    repeated_password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': False},
        }

    def validate(self, data):
        password = data.get('password')
        repeated_password = data.get('repeated_password')
        if password or repeated_password:
            if password != repeated_password:
                raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return data

    def update(self, instance, validated_data):
        if 'username' in validated_data and validated_data['username'].strip():
            instance.username = validated_data['username']
        if 'email' in validated_data and validated_data['email'].strip():
            instance.email = validated_data['email']
        if 'password' in validated_data and validated_data['password'].strip():
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
    



