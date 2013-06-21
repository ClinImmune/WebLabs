from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^$', DocumentList.to_view()),
	url(r'^/$')
) 
