from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainHoMe,name='Home'),
    # path('post', views.Single_Tweet,name='Single_tweet.html'),
]
