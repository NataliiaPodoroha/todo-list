import datetime

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    deadline = models.DateField(null=True)
    is_completed = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_completed", "-created_at"]

    def __str__(self):
        return self.content
