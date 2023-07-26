import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from todo.views import Todo
from django.contrib.auth import get_user_model
from datetime import date
from django.core.mail import send_mail
list = Todo.objects.filter(completed=False, duedate=date.today()).prefetch_related('author')
for todo in list:
    send_mail('Remainder: ' + todo.title, 'Hello ' + todo.author.username + ', \nToday is the duedate of your task "' + todo.title + 
              '". If you have completed the task, please check it as done\nRegards,\nTaskMate Team', 'noreply@mg.mohammedameen.tech',
              [todo.author.email])



