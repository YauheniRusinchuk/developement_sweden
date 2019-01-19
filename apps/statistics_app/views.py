from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
# Create your views here.
class Statistics(View):
    ''' Statistics page  '''

    def get(self, request, *args, **kwargs):
        return render(request, 'statistics/index.html', {})
