from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = patterns('',
	url(
		r'^$', 
		DocumentList.as_view(),
		name = 'document-list'
	),
	url(
		r'^(?P<pk>[0-9]+)/$', 
		DocumentDetail.as_view(),
		name = 'document-detail'	
	)
) 

urlpatterns = format_suffix_patterns(urlpatterns)

