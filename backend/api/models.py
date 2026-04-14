"""Описание моделей данных приложения API."""
from django.db import models


class Task(models.Model):
    """Модель задачи проекта Taski."""
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Возвращает строковое представление задачи."""
        return self.title
