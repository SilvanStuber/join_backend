from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from tasks_app.models import Task

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
