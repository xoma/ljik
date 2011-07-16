from django.conf.urls.defaults import *

from ljik.post.views import for_user, show, for_tag


urlpatterns = patterns('quotes',
    (r'^user/(?P<user_name>\w+)/$', for_user),
    (r'^tags/(?P<tag_name>\w+)/',for_tag),
    (r'^show/(?P<id>\d+)',show)
)