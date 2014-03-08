import mimetypes
from django.db import models

from django.core.files.storage import get_storage_class
from django_read import DJANGO_READ_STORAGE
from mptt.models import MPTTModel, TreeForeignKey

class Document(MPTTModel, models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    content_type = models.CharField(max_length=255, blank=True, null=True)
    resource = models.FileField(upload_to="files", storage=get_storage_class(DJANGO_READ_STORAGE)())
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
    	return "%s" % (self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('document_view', [str(self.id)])

    @property
    def extension(self):
        return mimetypes.guess_extension(self.content_type)
