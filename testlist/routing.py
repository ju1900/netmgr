from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/testlist/$', consumers.TestlistConsumer),
    url(r'^ws/product/(?P<id>[^/]+)/$', consumers.ProductConsumer),
    url(r'^ws/chapter/(?P<id>[^/]+)/$', consumers.ChapterConsumer),
    url(r'^ws/section/(?P<id>[^/]+)/$', consumers.SectionConsumer),
    url(r'^ws/testcase/(?P<id>[^/]+)/$', consumers.TestcaseConsumer),
]