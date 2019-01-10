from django.urls import path
from apps.notes.views import Index, DelelteNote, Complete

app_name = 'notes'

urlpatterns = [
    path('complete/<int:pk>/', Complete.as_view(), name='complete_page'),
    path('notesdelete/<int:pk>/', DelelteNote.as_view(), name='delete_note'),
    path('', Index.as_view(), name='notes_page'),
]
