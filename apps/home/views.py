import asyncio
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from apps.Profile.forms import RegisterForm
from django.contrib.auth.models import User
from apps.Profile.models import Profile
from apps.article.models import Article
from apps.comments.models import Comment
from apps.comments.forms import FormComment
from apps.home.forms import LoginForm
# Create your views here.


class Unsubscriptions(LoginRequiredMixin, View):
    ''' DELETE SUBSCRIDE  '''
    def get(self, request, *args, **kwargs):
        current_profile = Profile.objects.get(user=request.user)
        profile_del = Profile.objects.get(pk=kwargs['pk'])
        current_profile.subscriptions.remove(profile_del)
        return HttpResponseRedirect(reverse('home:detail_profile', kwargs={'pk': profile_del.pk}))


class Subscriptions(LoginRequiredMixin, View):
    ''' ADD SUBSCRIBE '''
    def get(self, request, *args, **kwargs):
        current_profile = Profile.objects.get(user=request.user)
        profile = Profile.objects.get(pk=kwargs['pk'])
        current_profile.subscriptions.add(profile)
        current_profile.save()
        return HttpResponseRedirect(reverse('home:detail_profile', kwargs={'pk': profile.pk}))


class DeleteProfile(LoginRequiredMixin, View):
    ''' Delete User and Profile '''
    def get(self, request, *args, **kwargs):
        user = User(pk=kwargs['pk'])
        if request.user == user:
            user.delete()
        return redirect('home:home_page')



class DeletePost(LoginRequiredMixin, View):
    ''' Delete Post '''
    def get(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        article.delete()
        return HttpResponseRedirect(reverse('home:detail_profile', kwargs={'pk': article.author.profile.pk}))


class EditPost(LoginRequiredMixin, View):
    ''' Update post  '''

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if request.user == article.author:
            return render(request, 'home/editpost.html', {'article' : article})
        else:
            return redirect('home:home_page')

    def post(self, request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        article.text = request.POST.get("edit")
        article.save()
        return HttpResponseRedirect(reverse('home:detail_profile', kwargs={'pk': article.author.profile.pk}))







class NewPost(LoginRequiredMixin, View):
    ''' New post '''

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        return render(request, 'profile/newpost.html', {'profile': profile})

    def post(self, request, *args, **kwargs):
        article = Article(author=request.user, text=request.POST.get('text'),
                img = request.FILES.get('images') or None)
        article.save();
        return redirect('home:home_page')



def result_article(profile):
    ''' Function return subscriptions articles '''
    # articlesresult = Article.objects.filter(author=[x.user for x in profile.subscriptions.all()])
    result = []
    articles = Article.objects.all()
    for sub in profile.subscriptions.all():
        for art in articles:
            if sub.user == art.author:
                result.append(art)
    result+= profile.user.article_set.all()
    return result



class Home(View):
    ''' Home page class '''
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            articles = result_article(profile)
            return render(request, 'home/index.html',
                {'profile': profile, 'articles': articles}
            )
        else:
            return render(request, 'home/guest.html', {})




class DetailProfile(LoginRequiredMixin, View):
    #model = Profile
    login_url = 'home:login_page'
    #template_name = 'home/detail.html'

    def get(self, request, *args, **kwargs):
        #profile_detail = Profile.objects.get(pk=kwargs['pk'])
        try:
            profile_detail = get_object_or_404(Profile, pk=kwargs['pk'])
        except Profile.DoesNotExist:
            raise Http404("No Profile matches the given query.")
        articles = Article.objects.filter(author=profile_detail.user)
        flag = False
        current_user = Profile.objects.get(user=request.user).subscriptions.all()
        if profile_detail in current_user:
            flag = True
        return render(request, 'home/detail.html',
            {'profile_detail': profile_detail, 'articles': articles, 'flag': flag}
        )

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #object = kwargs['object']
        #context['profile_detail'] = Profile.objects.get(pk=object.user.pk)
        #context['articles'] = Article.objects.filter(author=context['profile_detail'].user)
    #   return context



class Login(View):
    ''' Login User '''

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'home/login.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home_page')

            else:
                return redirect('home:login_page')
