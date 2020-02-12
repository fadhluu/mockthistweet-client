from django.urls import path
from . import controller

urlpatterns = [
    path('', controller.index, name="index"),
    path('new_tweet', controller.new_tweet, name="new tweet")
]
