from django.shortcuts import render, HttpResponse
from django.views import View
from apps.statistics_app.data.data import read_statistics
import json
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class Statistics(LoginRequiredMixin, View):
    ''' Statistics page  '''

    def get(self, request, *args, **kwargs):
        result = read_statistics(request.user.profile.pk)
        print(result)
        return render(request, 'statistics/index.html', {})



class StatisticsNotes(View):

    def get(self, request, *args, **kwargs):
        data = read_statistics(request.user.profile.pk)
        return HttpResponse(json.dumps(data), content_type='application/json')
