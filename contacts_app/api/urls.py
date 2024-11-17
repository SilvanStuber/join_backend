from django.contrib import admin
from django.urls import path, include
from .views import ContactsViewSets
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user_contacts', ContactsViewSets, basename='usercontact')

urlpatterns = [
    path('', include(router.urls)),
]