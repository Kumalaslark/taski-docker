"""Настройки административной панели для приложения API."""
from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Класс для управления задачами в панели администратора."""

    list_display = ('title', 'description', 'completed')
