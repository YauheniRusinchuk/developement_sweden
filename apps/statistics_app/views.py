from django.shortcuts import render, HttpResponse
from django.views import View
from apps.statistics_app.data.data import read_statistics
import json
# Create your views here.



class Statistics(View):
    ''' Statistics page  '''

    def get(self, request, *args, **kwargs):
        result = read_statistics(request.user.profile.pk)
        print(result)
        return render(request, 'statistics/index.html', {})



class StatisticsNote(View):

    def get(self, request, *args, **kwargs):
        pass
