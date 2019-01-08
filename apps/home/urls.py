from django.urls import path, include
from apps.home.views import (
    Home,
    Login,
    DetailProfile,
    NewPost,
    EditPost,
    DeletePost,
    DeleteProfile,
    Subscriptions,
    Unsubscriptions
)
from django.views.generic import TemplateView
from apps.article.views import DetailArticle
from apps.comments.views import DeleteComments

app_name = 'home'

urlpatterns = [
    path('deletecomment/<int:pk>/', DeleteComments.as_view(), name='delete_comment'),
    path('detailarticle/<int:pk>/', DetailArticle.as_view(), name='detail_article'),
    path('unsubscriptions/<int:pk>/', Unsubscriptions.as_view(), name='unsubscriptions_page'),
    path('subscriptions/<int:pk>/', Subscriptions.as_view(), name='subscriptions_page'),
    path('profile/id<int:pk>/', DetailProfile.as_view(), name='detail_profile'),
    path('editpost/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('deleteprofile/<int:pk>/', DeleteProfile.as_view(), name='delete_profile'),
    path('deletepost/<int:pk>/', DeletePost.as_view(), name='delete_post'),
    path('younewpost/', NewPost.as_view(), name='newpost_page'),
    path('login/', Login.as_view(), name='login_page'),
    path('about/', TemplateView.as_view(template_name="home/about.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="home/contact.html"), name='contact'),
    path('', Home.as_view(), name='home_page'),
]
