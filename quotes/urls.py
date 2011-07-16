from django.conf.urls.defaults import *

from ljik.quotes.views import for_user, show, for_tag

urlpatterns = patterns('quote',
    (r'^user/(?P<user_name>\w+)/$',for_user),
    (r'^show/(?P<id>\d+)',show),
    (r'^tags/(?P<tag_name>\w+)/',for_tag),
)