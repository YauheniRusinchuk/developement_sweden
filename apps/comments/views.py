from django.shortcuts import render, redirect
from django.views import View
from apps.comments.models import Comment

# Create your views here.
class DeleteComments(View):

    ''' Delete comment '''


    def get(self, request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if request.user == comment.author:
            comment.delete()
        return redirect('home:home_page')
