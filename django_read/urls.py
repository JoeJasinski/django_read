from django.conf.urls import patterns, url
from django_read.views import DocumentDetailView, DocumentContentView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/content/$', DocumentContentView.as_view(), {}, name="document_content_view"),
    url(r'^(?P<pk>\d+)/$', DocumentDetailView.as_view(), {}, name="document_view"),
)