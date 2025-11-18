from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title