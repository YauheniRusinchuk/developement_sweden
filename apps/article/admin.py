from django.contrib import admin

# Register your models here.
from apps.article.models import Article

admin.site.register(Article)
