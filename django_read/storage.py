from django.core.files.storage import FileSystemStorage
from django_read import DJANGO_READ_MEDIA_ROOT, DJANGO_READ_MEDIA_URL
from mptt.models import MPTTModel, TreeForeignKey


class DjangoReadFileSystemStorage(FileSystemStorage):

    def __init__(self, location=None, base_url=None, *args, **kwargs):
        location=DJANGO_READ_MEDIA_ROOT
        base_url=DJANGO_READ_MEDIA_URL
    	super(DjangoReadFileSystemStorage, self).__init__(
    		location=location, base_url=base_url, *args, **kwargs) 




