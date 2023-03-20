# Generated by Django 4.1.7 on 2023-03-19 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todo", "0003_alter_todo_options_todo_author_todo_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
