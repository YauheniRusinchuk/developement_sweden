from django.shortcuts import render
from django.views import View
from apps.statistics_app.data.data import read_statistics

# Create your views here.



class Statistics(View):
    ''' Statistics page  '''

    def get(self, request, *args, **kwargs):
        result = read_statistics(request.user.profile.pk)
        print(result)
        return render(request, 'statistics/index.html', {})
