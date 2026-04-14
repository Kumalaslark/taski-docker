"""Представления (Views) для обработки запросов API."""
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Набор представлений для работы с задачами."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        """Логика при создании новой задачи."""
        serializer.save()
