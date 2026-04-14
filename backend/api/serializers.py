"""Сериализаторы для преобразования моделей API в JSON и обратно."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Task."""

    class Meta:
        """Мета-параметры сериализатора Task."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
