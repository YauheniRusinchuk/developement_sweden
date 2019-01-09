from django.shortcuts import render
from django.views import View
from apps.notes.forms import FormNote
# Create your views here.
class Index(View):
    ''' Index get notes '''

    def get(self, request, *args, **kwargs):
        form = FormNote()
        return render(request, 'notes/index.html', {'form': form})
