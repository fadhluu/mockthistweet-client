from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new_tweet', views.new_tweet, name="new tweet")
]
