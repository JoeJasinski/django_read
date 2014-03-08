from django.conf import settings

DJANGO_READ_MEDIA_ROOT = getattr(settings, 'DJANGO_READ_MEDIA_ROOT', settings.MEDIA_ROOT)
DJANGO_READ_STORAGE = getattr(settings, 'DJANGO_READ_STORAGE', "django_read.storage.DjangoReadFileSystemStorage")
DJANGO_READ_MEDIA_URL = getattr(settings, 'DJANGO_READ_MEDIA_URL', settings.MEDIA_URL)
DJANGO_READ_PRIVATE = getattr(settings, "DJANGO_READ_PRIVATE", False)


DJANGO_READ_UPLOAD_CONTENT_TYPES = getattr(settings, 'DJANGO_READ_UPLOAD_CONTENT_TYPES', 
	['application/epub+zip', 'application/pdf'])
DJANGO_READ_UPLOAD_FILE_MAX_SIZE = getattr(settings, 'DJANGO_READ_UPLOAD_FILE_MAX_SIZE', 5242880)
