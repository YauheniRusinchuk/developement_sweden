from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    ''' Index get notes '''

    def get(self, request, *args, **kwargs):
        return render(request, 'notes/index.html', {})
