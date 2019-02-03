from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from apps.Profile.forms import RegisterForm
from django.contrib.auth.models import User
from apps.Profile.models import Profile
from apps.statistics_app.data.data import write_new_person

# Create your views here.

class UserRegister(View):
    ''' Registration new user and profile '''

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'profile/registration.html', {'form': form})


    def post(self, request, *args, **kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        user = User.objects.create_user(username=username)
        user.first_name = firstname
        user.last_name = lastname
        user.set_password(password)
        user.save()
        profile = Profile(user=user)
        profile.save()
        write_new_person(profile.pk, profile.user.username)
        return HttpResponse('success python')
