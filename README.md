IN PROGRESS


This Django module is designed to be a simple mechanism to host private ebooks online.
Currently, staff users can upload Documents via Django admin. 


## REQUIREMENTS
 - Django 1.6 (tested with 1.6, but could work with others)
 - django-mptt-admin module
 - South (optional)

## INSTALLATION

Add the following to INSTALLED_APPS in settings.py:

    'south',
    'django_mptt_admin',
    'django_read',

Add the following to urls.py:

    url(r'^documents/', include('django_read.urls')),

If using South, execute the following:
    
    ./manage.py syncdb 
    ./manage.py migrate django_read

Or when just using syncdb:

    ./manage.py syncdb 



CONFIGURATION


DJANGO_READ_MEDIA_ROOT = (default MEDIA_ROOT) - this is the directory that files will be 
  uploaded to.  This defaults to the MEDIA_ROOT, but if your files are private, 
  you should set this to a private directory.  You will also need to configure Nginx
  to serve these files privately.  See the Nginx sestion below. 

DJANGO_READ_UPLOAD_CONTENT_TYPES = (default ['application/epub+zip', 'application/pdf']) -
  These are the file types that this application will accept as uploads. 

DJANGO_READ_UPLOAD_FILE_MAX_SIZE = (default 5242880) - this is the maximum upload size
  (in bytes) that this application will accept. 

DJANGO_READ_MEDIA_URL = (default "/protected/") - If you wish to serve these files
  privately, this is the URL root that you will need to configure Nginx to serve from.
  See the Nginx config example below.


This codebase also contains an example django project with the default configuration.



http://wiki.nginx.org/XSendfile

    location /static {
      root /path/to/htdocs;
      access_log off;
    }
    location /media {
      root /path/to/htdocs;
      access_log off;
    }

    location /protected/ {
      internal;
      alias   /path/to/private/documents;
    }