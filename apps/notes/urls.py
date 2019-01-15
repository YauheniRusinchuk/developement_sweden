from django.urls import path, include
from apps.notes.views import Index, DelelteNote, Complete


app_name = 'notes'

urlpatterns = [
    path('mystatistics/', include('apps.statistics_app.urls', namespace='statistics')),
    path('complete/<int:pk>/', Complete.as_view(), name='complete_page'),
    path('notesdelete/<int:pk>/', DelelteNote.as_view(), name='delete_note'),
    path('', Index.as_view(), name='notes_page'),
]
