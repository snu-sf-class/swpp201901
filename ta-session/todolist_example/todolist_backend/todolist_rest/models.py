from django.db import models

# Create your models here.
class Todo(models.Model):
    contents = models.TextField()
    done = models.BooleanField()
