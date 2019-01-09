from django.urls import path
from apps.notes.views import Index

app_name = 'notes'

urlpatterns = [
    path('', Index.as_view(), name='notes_page'),
]
