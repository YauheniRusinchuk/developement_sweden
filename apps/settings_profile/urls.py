from django.urls import path
from apps.settings_profile.views import Settings


app_name = 'settings'


urlpatterns = [
    path('profile/id<int:pk>/', Settings.as_view(), name='settings_page'),
]
