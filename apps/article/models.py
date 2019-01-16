from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
import apps.comments.models
from django.db.models.signals import pre_delete, post_delete, pre_save
from django.dispatch import receiver
import os

# Create your models here.
class Article(models.Model):

    ''' I is a article model '''

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='img_article/', blank=True)

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


@receiver(pre_save, sender=Article)
def update_to_img_article(sender, instance, **kwargs):
    if not instance.img:
        return False

    old_file = sender.objects.get(author=instance.author).img or None

    if old_file:
        if not old_file == instance.img:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)



@receiver(post_delete, sender=Article)
def my_signal(sender, instance, **kwargs):
        if instance.img:
            if os.path.isfile(instance.img.path):
                os.remove(instance.img.path)
        else:
            print('NOT IMG')
