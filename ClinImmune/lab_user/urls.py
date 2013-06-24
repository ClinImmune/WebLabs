from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from lab_user import views

urlpatterns = patterns('',
#    url(r'^new/$', views.NewUser.as_view()),
#    url(r'^/$', views.UserList.as_view()), # Lists users by most recent job
#    url(r'(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

