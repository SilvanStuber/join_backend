from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from tasks_app.models import Task

"""
ViewSet for providing a summary of tasks related to the authenticated user.

Inherits:
    ViewSet: Base class for custom views in DRF.

Attributes:
    permission_classes (list): Enforces IsAuthenticated permission.

Methods:
    list(request):
        - Retrieves a summary of tasks created by or assigned to the authenticated user.
        - Calculates:
            - total_tasks: Total number of tasks.
            - todo_tasks: Number of tasks with 'todo' status.
            - in_progress_tasks: Number of tasks with 'inProgress' status.
            - await_feedback_tasks: Number of tasks with 'awaitFeedback' status.
            - done_tasks: Number of tasks with 'done' status.
            - priority_urgent_tasks: Number of tasks marked as 'priorityUrgent'.
            - closest_due_date: Due date of the most urgent task, if any.

Returns:
    Response: A JSON object containing the task summary.
"""
class TaskSummaryViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        user_tasks = Task.objects.filter(
            Q(creator=user) |
            Q(assigned__icontains=user.username)
        )
        total_tasks = user_tasks.count()
        todo_tasks = user_tasks.filter(task_status='todo').count()
        in_progress_tasks = user_tasks.filter(task_status='inProgress').count()
        await_feedback_tasks = user_tasks.filter(task_status='awaitFeedback').count()
        done_tasks = user_tasks.filter(task_status='done').count()
        priority_urgent_tasks = user_tasks.filter(priority_content='priorityUrgent').count()
        urgent_task = user_tasks.filter(priority_content='priorityUrgent').order_by('due_date').first()
        closest_due_date = urgent_task.due_date if urgent_task else None
        return Response({
            "total_tasks": total_tasks,
            "todo_tasks": todo_tasks,
            "in_progress_tasks": in_progress_tasks,
            "await_feedback_tasks": await_feedback_tasks,
            "done_tasks": done_tasks,
            "priority_urgent_tasks": priority_urgent_tasks,
            "closest_due_date": closest_due_date,
        })
