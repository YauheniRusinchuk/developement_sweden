from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.home.views import (
    Home,
    NewPost,
    DetailProfile,
    EditPost,
    DeletePost,
    DeleteProfile,
    Login
)

from apps.article.views import DetailArticle
from apps.comments.views import DeleteComments
from apps.Profile.views import UserRegister


class TestUrlsHome(SimpleTestCase):

    def test_url_simple(self):
        url = reverse('home:home_page')
        self.assertEquals(resolve(url).func.view_class, Home)


    def test_url_add_post(self):
        url = reverse('home:newpost_page')
        self.assertEquals(resolve(url).func.view_class, NewPost)


    def test_url_detail_profile(self):
        url = reverse('home:detail_profile', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DetailProfile)

    def test_url_delete_profile(self):
        url = reverse('home:delete_profile', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DeleteProfile)

    def test_url_edit_post(self):
        url = reverse('home:edit_post', args=['1'])
        self.assertEquals(resolve(url).func.view_class, EditPost)


    def test_url_delete_post(self):
        url = reverse('home:delete_post', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DeletePost)


    def test_url_detail_article(self):
        url = reverse('home:detail_article', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DetailArticle)

    def test_url_delete_comment(self):
        url = reverse('home:delete_comment', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DeleteComments)

    def test_url_login(self):
        url = reverse('home:login_page')
        self.assertEquals(resolve(url).func.view_class, Login)



class TextUrlsProfile(SimpleTestCase):

    def test_url_profile_home(self):
        url = reverse('profile:registration_page')
        self.assertEquals(resolve(url).func.view_class, UserRegister)
