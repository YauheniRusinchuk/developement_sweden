from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponseRedirect
from apps.comments.models import Comment


class UpdateComment(View):
    pass



# Create your views here.
class DeleteComments(View):

    ''' Delete comment '''


    def get(self, request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if request.user == comment.author:
            comment.delete()
        return HttpResponseRedirect(reverse('home:detail_article', kwargs={'pk': comment.article.pk}))
