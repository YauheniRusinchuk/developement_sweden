from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from apps.article.models import Article
from apps.notes.models import Note
import datetime
import os
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    subscriptions = models.ManyToManyField('self', related_name="Subscriptions", symmetrical=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-timestamp']


    @property
    def fullname(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"Profile : {self.user.username}"

    def count(self):
        return Article.objects.filter(author=self.user).count()

    def count_subscriptions(self):
        return self.subscriptions.count()


    def last_five_sub(self):
        return self.subscriptions.all()


    def my_notes(self):
        notes = Note.objects.filter(user=self.user).filter(
            timestamp=datetime.datetime.now().date()
        )

        return notes

# 
# @receiver(post_save, sender=Profile)
# def create_profile_statistics(sender, instance, **kwargs):
#     print('create statistics_profile')
#     statistics_profile = StatisticsNotes(profile=instance.user)
#     statistics_profile.save()
#     print('complete ....')



@receiver(pre_save, sender=Profile)
def auto_delete_pre_save(sender, instance, **kwargs):
    if not instance.avatar:
         return False
    old_file = sender.objects.get(user=instance.user).avatar or None

    if old_file:
        if not old_file == instance.avatar:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


@receiver(post_delete, sender=Profile)
def my_signal(sender, instance, **kwargs):
        if instance.avatar:
            if os.path.isfile(instance.avatar.path):
                os.remove(instance.avatar.path)
        else:
            print('NOT IMG')
