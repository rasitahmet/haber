from django.conf.urls import patterns, include, url

urlpatterns = patterns('haber.views',
    url(r'^$', 'index'),
    url(r'^(?P<haber_id>\d+)/$', 'icerik'),
)
