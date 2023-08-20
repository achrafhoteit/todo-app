from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateField(auto_now_add=False)
    deadline_time = models.TimeField(auto_now_add=False)
    # Many to One relationship for the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def is_end_date(self):
        end_date = datetime.combine(self.deadline_date, self.deadline_time)
        if datetime.now() > end_date and self.completed is False:
            return True
        else:
            return False

    class Meta:
        ordering = ['completed', ] # Completed tasks are sent to the bottom of the list

