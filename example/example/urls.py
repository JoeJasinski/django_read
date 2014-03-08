from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django_read import DJANGO_READ_MEDIA_ROOT, DJANGO_READ_MEDIA_URL

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^documents/', include('django_read.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 