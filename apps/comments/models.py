from django.db import models
from django.contrib.auth.models import User
from apps.article.models import Article
# Create your models here.



class Comment(models.Model):

    author  = models.OneToOneField(User, on_delete=models.CASCADE)
    text    = models.TextField(blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment in {self.article} user {self.author}"
