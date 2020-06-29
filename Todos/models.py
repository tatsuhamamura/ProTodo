from django.db import models
from django.utils import timezone

# Create your models here.

class TodoItem(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    target_timestamp = models.DateTimeField()
    btc = models.DateTimeField(auto_now=True)
    todo_status = models.BooleanField(db_index=True, default=True)

