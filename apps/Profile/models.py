from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.article.models import Article
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    subscriptions = models.ManyToManyField('self', related_name="Subscriptions", symmetrical=False)


    @property
    def fullname(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"Profile : {self.user.username}"

    def count(self):
        return Article.objects.filter(author=self.user).count()

    def count_subscriptions(self):
        return self.subscriptions.count()

    @property
    def last_five_sub(self):
        return self.subscriptions.all()[::-1][:5]





# @receiver(signals.post_delete, sender=Profile)
# def delete_profile(sender, instance, **kwargs):
#     if instance.avatar.path:
#         storage = instance.avatar.storage
#         path = instance.avatar.path
#         storage.delete(path)
#     else:
#         instance.delete()
