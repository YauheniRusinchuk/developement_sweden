from django.shortcuts import render
from django.views import View
# Create your views here.
class Statistics(View):
    ''' Statistics page  '''

    def get(self, request, *args, **kwargs):
        return render(request, 'statistics/index.html', {})
