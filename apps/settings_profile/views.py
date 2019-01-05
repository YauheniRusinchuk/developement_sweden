from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.Profile.models import Profile
from django.contrib.auth.models import User
# Create your views here.


class Settings(LoginRequiredMixin, View):

    login_url = 'home:home_page'

    ''' Settings profile if user.request == this profile '''

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if request.user == user:
            profile = Profile.objects.get(user=user)
            return render(request, 'profile/settings.html', {'profile': profile})
        else:
            return redirect('home:home_page')


    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.save()
        profile = Profile.objects.get(user=user)
        avatar = profile.avatar
        if request.FILES:
            profile.avatar = request.FILES['image']
        else:
            profile.avatar = avatar
        profile.description = request.POST.get('description')
        profile.save()
        return HttpResponseRedirect(reverse('home:detail_profile', kwargs={'pk': user.pk}))
