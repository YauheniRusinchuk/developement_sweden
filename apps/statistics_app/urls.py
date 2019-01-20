from django.urls import path
from apps.statistics_app.views import Statistics, StatisticsNotes

app_name = 'statistics'

urlpatterns = [
    path('result/', StatisticsNotes.as_view(), name='statistics_note_page'),
    path('', Statistics.as_view(), name='statistics_page'),
]
