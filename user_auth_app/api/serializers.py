from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

"""
Serializer for the UserProfile model.

Attributes:
    username (CharField): Read-only field to display the associated user's username.

Meta:
    model (Model): Specifies the User model to be serialized.
    fields (list): Defines the fields to include in the serialized output:
        - user: Reference to the User object.
        - email: Email address of the user profile.
        - phone: Phone number of the user profile.
"""
class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = User
        fields = ['user', 'email', 'phone']

"""
Serializer for handling user registration.

Attributes:
    repeated_password (CharField): Field for confirming the password during registration.

Meta:
    model (Model): Specifies the User model to be serialized.
    fields (list): Includes:
        - username: The username of the user.
        - email: The email address of the user.
        - password: The user's password (write-only).
        - repeated_password: Confirmation of the password (write-only).
    extra_kwargs (dict): Makes the password write-only.

Methods:
    save():
        - Validates that the password and repeated_password match.
        - Checks if the email is already registered.
        - Creates a new user account with the provided email, username, and password.
        - Returns the newly created User instance.
        - Raises ValidationError if passwords do not match or if the email is already in use.
"""
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

"""
Serializer for handling custom login with email and password authentication.

Attributes:
    email (EmailField): User's email address for authentication.
    password (CharField): User's password (write-only).

Methods:
    validate(data):
        - Ensures both email and password are provided.
        - Checks if the email exists in the database.
        - Authenticates the user with the provided email and password.
        - Returns the user if authentication is successful.
        - Raises ValidationError if:
            - Email or password is missing.
            - Email does not exist.
            - Authentication fails due to invalid credentials.
"""
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
    
"""
Serializer for updating user information, including optional password change.

Attributes:
    password (CharField): Optional, write-only field for the new password.
    repeated_password (CharField): Optional, write-only field for confirming the new password.

Meta:
    model (Model): Specifies the User model to be serialized.
    fields (list): Includes:
        - username: The user's username (optional).
        - email: The user's email (optional).
        - password: The new password (optional).
        - repeated_password: Confirmation for the new password (optional).
    extra_kwargs (dict): Makes username and email optional fields.

Methods:
    validate(data):
        - Ensures that if a password is provided, it matches the repeated_password.
        - Returns validated data or raises a ValidationError if passwords do not match.

    update(instance, validated_data):
        - Updates the username, email, or password if provided in validated_data.
        - Ensures password is hashed using `set_password`.
        - Saves and returns the updated user instance.
"""
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
    



