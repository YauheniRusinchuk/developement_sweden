from django.shortcuts import render, redirect
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
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username)
            user.first_name = first_name
            user.last_name = last_name
            user.set_password(password)
            user.save()
            profile = Profile(user=user)
            profile.save()
            write_new_person(profile.pk, profile.user.username)
        return redirect('home:login_page')
