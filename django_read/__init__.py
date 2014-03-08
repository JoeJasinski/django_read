from django.conf import settings

DJANGO_READ_FILES = getattr(settings, 'DJANGO_READ_FILES', settings.MEDIA_ROOT)
DJANGO_READ_UPLOAD_CONTENT_TYPES = getattr(settings, 'DJANGO_READ_UPLOAD_CONTENT_TYPES', ['application/epub+zip','application/epub', 'application/pdf'])
DJANGO_READ_UPLOAD_FILE_MAX_SIZE = getattr(settings, 'DJANGO_READ_UPLOAD_FILE_MAX_SIZE', 5242880)