from django.conf.urls.defaults import *

urlpatterns = patterns(
    'simplenews.views',
    url(r'^$', 'object_list', {}, name='news_list'),
    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', {}, name='news_detail'),
    )
