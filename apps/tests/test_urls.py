from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.home.views import Home


class TestUrls(SimpleTestCase):

    def test_url_simple(self):
        url = reverse('home:home_page')
        self.assertEquals(resolve(url).func.view_class, Home)
