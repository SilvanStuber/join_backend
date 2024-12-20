from django.contrib import admin
from django.urls import path, include
from .views import TasksViewSets
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TasksViewSets, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]