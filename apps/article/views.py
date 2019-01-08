from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.article.models import Article
from django.views import View
from apps.comments.models import Comment
from apps.comments.forms import FormComment
# Create your views here.
class DetailArticle(LoginRequiredMixin, View):
    ''' Detail article view '''

    def get(self,request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        form = FormComment()
        return render(request, 'article/detail.html',
            {'article': article, 'form': form}
        )

    def post(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        form = FormComment(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment = Comment(author=request.user, text=text, article=article)
            comment.save()
        return HttpResponseRedirect(reverse('home:detail_article', kwargs={'pk': article.pk}))
