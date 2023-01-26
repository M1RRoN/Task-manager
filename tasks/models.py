from django.db import models
from labels.models import Label
from statuses.models import Status
from users.models import CustomUser


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = models.TextField(null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True)
    executor = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, related_name='executor')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Label, through='Relations', blank=True)

    def __str__(self):
        return self.name


class Relations(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    labels = models.ForeignKey(Label, on_delete=models.PROTECT, null=True)
