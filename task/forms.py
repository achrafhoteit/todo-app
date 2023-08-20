from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'completed', 'deadline_date', 'deadline_time']
        widgets = {
            'deadline_date': forms.DateInput(attrs={'type': 'date'}),
            'deadline_time': forms.TimeInput(attrs={'type': 'time'}),
        }
