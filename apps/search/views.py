from django.shortcuts import render
from django.views import View

# Create your views here.
class Search(View):

    ''' Search view '''

    def get(self, request, *args, **kwargs):
        return render(request, 'search/search.html', {})
