from django.urls import path, include
from apps.Profile.views import UserRegister

app_name = 'profile'

urlpatterns = [
    path('', UserRegister.as_view(), name='registration_page'),
]
