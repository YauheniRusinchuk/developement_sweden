from django.shortcuts import render
from django.views import View
from apps.statistics_app.data.statistics_table import StatisticsFile
# Create your views here.
class Statistics(View):
    ''' Statistics page  '''

    def get(self, request, *args, **kwargs):
        instance_csv = StatisticsFile()
        result = dict(instance_csv.read(str(request.user.profile.pk)))
        for k,v in result.items():
            print(k, v)
        return render(request, 'statistics/index.html', {})



class StatisticsCsvInfo(View):
    pass
