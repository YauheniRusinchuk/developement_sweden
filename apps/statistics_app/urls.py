from django.urls import path
from apps.statistics_app.views import Statistics

app_name = 'statistics'

urlpatterns = [
    path('', Statistics.as_view(), name='statistics_page'),
]
