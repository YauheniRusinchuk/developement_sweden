from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    ''' Model Note '''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    timestamp = models.DateField(auto_now=False)
    create = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']


    def __str__(self):
        return f"User {self.user} create note "
