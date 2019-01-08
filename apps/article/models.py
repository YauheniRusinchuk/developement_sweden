from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
import apps.comments.models

# Create your models here.
class Article(models.Model):

    ''' I is a article model '''

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('home:detail_article', kwargs={'pk': self.pk})


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Article user : {self.author.username}"

    @property
    def comments(self):
        return apps.comments.models.Comment.objects.filter(article=self)

    @property
    def count_comments(self):
        return apps.comments.models.Comment.objects.filter(article=self).count()
