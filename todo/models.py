from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    creator = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
