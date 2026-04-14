from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Начальная миграция для проекта Taski.

    Создает модель Task с полями title, description и status.
    """

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120,
                                           verbose_name='Заголовок')),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
