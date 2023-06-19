from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Todos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["completed"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todos_detail", kwargs={"pk": self.pk})
