from django.conf.urls.defaults import *

from ljik.links.views import show, for_tag


urlpatterns = patterns('link',
    (r'^show/(?P<id>\d+)',show),
    (r'^tags/(?P<tag_name>\w+)/',for_tag),
)