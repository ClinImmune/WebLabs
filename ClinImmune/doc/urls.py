from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(
		r'^$', 
		DocumentList.as_view()
	),
	url(
		r'^(?P<doc_id>\d+)/$', 
		DocumentDetail.as_view()
	),
	url(
		r'^(?P<doc_id>\d+)/(?P<chap_id>\d+)/', 
		ChapterDetail.as_view()
	),
	url(
		r'^(?P<doc_id>\d+)/(?P<chap_id>\d+)/(?P<sec_id>\d+)',
		SectionDetail.as_view()
	),
) 

