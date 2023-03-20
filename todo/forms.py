from django import forms
from .models import Todo
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    class  Meta:
        model = Todo
        fields = ("title", "duedate")
        widgets = {
            'duedate' : DateInput(attrs={'class' : 'todo-form-date', 'value' : date.today() }),
            'title' : forms.TextInput(attrs={'class' : 'todo-form-title'})
        }
        labels = {
            'duedate' : '',
            'title' : '',
        }

