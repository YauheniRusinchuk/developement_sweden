from django.shortcuts import render, redirect
from apps.article.models import Article
from django.views import View
from apps.comments.models import Comment
from apps.comments.forms import FormComment
# Create your views here.
class DetailArticle(View):
    ''' Detail article view '''

    def get(self,request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        form = FormComment()
        print(article.comments)
        return render(request, 'article/detail.html',
            {'article': article, 'form': form}
        )

    def post(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        form = FormComment(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
        return redirect('home:home_page')
