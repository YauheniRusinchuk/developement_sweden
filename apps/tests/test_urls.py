from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.home.views import Home, NewPost


class TestUrls(SimpleTestCase):

    def test_url_simple(self):
        url = reverse('home:home_page')
        self.assertEquals(resolve(url).func.view_class, Home)


    def test_url_add_post(self):
        url = reverse('home:newpost_page')
        self.assertEquals(resolve(url).func.view_class, NewPost)
