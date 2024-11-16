from django.contrib import admin
from django.urls import path, include
from .views import TasksViewSets
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TasksViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
