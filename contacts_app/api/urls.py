from django.contrib import admin
from django.urls import path, include
from .views import ContactsViewSets
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user_contacts', ContactsViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
