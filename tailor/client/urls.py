from django.conf.urls.defaults import patterns, include, url
from tailor.client.views import schema

urlpatterns = patterns('',    
    url(r'^api/v1/schema/$', schema, name='schema'),
)
