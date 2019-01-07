from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from apps.article.models import Article

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
            return render(request, 'search/search.html', {'articles': articles})
        return redirect('home:home_page')
