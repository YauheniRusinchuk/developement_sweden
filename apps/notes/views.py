from django.shortcuts import render, redirect
from django.views import View
from apps.notes.forms import FormNote
from apps.notes.models import Note

# Create your views here.

class DelelteNote(View):
    ''' Delte note '''

    def get(self, request, *args, **kwargs):
        note = Note.objects.get(pk=kwargs['pk'])
        if request.user == note.user:
            note.delete()
        return redirect('notes:notes_page')





class Index(View):
    ''' Index get notes '''

    def get(self, request, *args, **kwargs):
        form = FormNote()
        notes = Note.objects.filter(user=request.user)
        return render(request, 'notes/index.html', {'form': form, 'notes': notes})


    def post(self, request, *args, **kwargs):
        form = FormNote(request.POST)
        if form.is_valid():
            description = form.cleaned_data['body']
            timestamp = form.cleaned_data['time']
            note = Note(user=request.user, description=description, timestamp=timestamp)
            note.save()
            return redirect('notes:notes_page')
