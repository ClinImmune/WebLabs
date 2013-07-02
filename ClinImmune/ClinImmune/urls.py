from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^users/', include('lab_user.urls')),
    url(r'^docs/', include('doc.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^jobs/', include('job.urls'))
)
