from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskSummaryViewSet

router = DefaultRouter()
router.register(r'summary', TaskSummaryViewSet, basename='summary_data')

urlpatterns = [
    path('', include(router.urls)),
]
