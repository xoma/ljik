from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf    import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','ljik.views.index'),

    (r'^quotes/(?P<user_name>\w+)/$','ljik.quotes.views.for_user'),
    (r'^posts/(?P<user_name>\w+)/$','ljik.post.views.for_user'),
    (r'^links/(?P<user_name>\w+)/$','ljik.links.views.for_user'),

    (r'quote/',include('ljik.quotes.urls')),
    (r'post/',include('ljik.post.urls')),
    (r'link/',include('ljik.links.urls')),
    (r'blog/',include('ljik.blog.urls')),
    (r'^back/', include(admin.site.urls)),
	(r'^web/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DOC_ROOT}),
)

