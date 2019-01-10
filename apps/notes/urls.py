from django.urls import path
from apps.notes.views import Index, DelelteNote

app_name = 'notes'

urlpatterns = [
    path('notesdelete/<int:pk>/', DelelteNote.as_view(), name='delete_note'),
    path('', Index.as_view(), name='notes_page'),
]
