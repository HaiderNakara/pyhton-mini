from django.db import models

# Create your models here.


class Todo(models.Model):
    content = models.TextField()
    type = models.TextField()
    subject = models.TextField()

    def __str__(self):
        return self.content
