from django.urls import path
from apps.search.views import Search

app_name = 'search'


urlpatterns = [
    path('', Search.as_view(), name='search_page'),
]
