from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^$', JobList.as_view()),
	url(r'^(?P<job_id>)/$', JobDetail.as_view()),
)
