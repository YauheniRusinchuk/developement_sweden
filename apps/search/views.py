from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from apps.article.models import Article
from django.contrib.auth.models import User

# Create your views here.
class Search(View):

    ''' Search view '''

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            articles = Article.objects.filter(
                Q(text__icontains=query) |
                Q(text__startswith=query) |
                Q(text__istartswith=query) |
                Q(text__endswith=query) |
                Q(text__iendswith=query)
            )
            users = User.objects.filter(
                Q(first_name__icontains=query) |
                Q(first_name__startswith=query) |
                Q(first_name__istartswith=query) |
                Q(first_name__endswith=query) |
                Q(first_name__iendswith=query) |
                Q(last_name__icontains=query) |
                Q(last_name__startswith=query) |
                Q(last_name__istartswith=query) |
                Q(last_name__endswith=query) |
                Q(last_name__iendswith=query)

            )
            return render(request, 'search/search.html', {'articles': articles, 'users': users})
        return redirect('home:home_page')
