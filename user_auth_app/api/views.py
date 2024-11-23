from rest_framework import generics
from user_auth_app.models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, CustomLoginSerializer, UpdateUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateAPIView

"""
API view for listing and creating UserProfile objects.

Inherits:
    generics.ListCreateAPIView: Provides GET (list) and POST (create) functionality.

Attributes:
    queryset (QuerySet): Retrieves all UserProfile objects from the database.
    serializer_class (Serializer): Specifies the UserProfileSerializer for serialization and deserialization.
"""
class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

"""
API view for retrieving, updating, and deleting a specific UserProfile object.

Inherits:
    generics.RetrieveUpdateDestroyAPIView: Provides GET (retrieve), PUT/PATCH (update), and DELETE functionality.

Attributes:
    queryset (QuerySet): Retrieves all UserProfile objects from the database.
    serializer_class (Serializer): Specifies the UserProfileSerializer for serialization and deserialization.
"""
class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


"""
API view for user registration.

Inherits:
    APIView: Provides methods for handling HTTP requests.

Attributes:
    permission_classes (list): Allows unrestricted access with AllowAny permission.

Methods:
    post(request):
        - Handles POST requests to register a new user.
        - Validates the input data using the RegistrationSerializer.
        - If valid:
            - Saves the new user account.
            - Creates or retrieves an authentication token for the new user.
            - Returns a response containing:
                - Authentication token.
                - Username.
                - Email.
        - If invalid:
            - Returns a response containing validation errors.
"""
class RegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request): 
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email
            }
        else:
            data=serializer.errors      
        return Response(data)
    
"""
Custom login view for user authentication and token generation.

Inherits:
    ObtainAuthToken: Extends functionality for token-based authentication.

Attributes:
    permission_classes (list): Allows unrestricted access with AllowAny permission.
    serializer_class (Serializer): Specifies the CustomLoginSerializer for validating email and password.

Methods:
    post(request):
        - Handles POST requests for user login.
        - Validates user credentials using the CustomLoginSerializer.
        - If valid:
            - Retrieves or creates an authentication token for the user.
            - Returns a response containing:
                - Authentication token.
                - User ID.
                - Username.
                - Email.
        - If invalid:
            - Returns a response containing validation errors.
"""
class CostomLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    serializer_class = CustomLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'id': user.pk,
                'username': user.username,
                'email': user.email
            }
        else:
            data=serializer.errors  
        return Response(data)


"""
API view for retrieving and updating user details.

Inherits:
    RetrieveUpdateAPIView: Provides functionality for GET (retrieve) and PUT/PATCH (update) requests.

Attributes:
    queryset (QuerySet): Retrieves all User objects from the database.
    serializer_class (Serializer): Specifies the UpdateUserSerializer for handling user data.
    permission_classes (list): Ensures the user is authenticated with IsAuthenticated permission.
"""
class UpdateUserView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]
    