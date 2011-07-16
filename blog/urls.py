from django.conf.urls.defaults import *
from ljik.blog.views import show

urlpatterns = patterns('blog',
    (r'^show/(?P<id>\d+)',show),
)