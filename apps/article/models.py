from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):

    ''' I is a article model '''

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Article user : {self.author.username}"
