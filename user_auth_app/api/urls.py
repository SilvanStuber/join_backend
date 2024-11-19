from django.urls import path
from .views import UserProfileList, UserProfileDetail, RegistrationView, CostomLoginView, UpdateUserView


urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', CostomLoginView.as_view(), name='login'),
    path('update-user/<int:pk>/', UpdateUserView.as_view(), name='update-user-by-pk'),
]