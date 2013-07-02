from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', AboutListView.as_view()),
    url(r'^(?<about_id>\d+)/', AboutDetailView.as_view()),
)
