from django.db import models
from datetime import date
import uuid, calendar

class Todo(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    duedate = models.DateField()

    @property
    def is_past(self):
        return self.duedate < date.today() 
    
    @property
    def is_completed(self):
        return self.completed

    def formatted_date(self):
        curr = self.duedate.strftime("%a, %d ")
        month = self.duedate.month
        curr += calendar.month_abbr[month]
        return curr


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed', '-id']
