from django.conf.urls import patterns, url
from django_read.views import DocumentDetailView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', DocumentDetailView.as_view(), {}, name="document_view"),
)