from django.contrib import admin
from django import forms
from django.shortcuts import render
from django.conf.urls import patterns, url
from django_mptt_admin.admin import DjangoMpttAdmin
from django_read.models import Document
from django.utils.translation import ugettext as _
from django.template.defaultfilters import filesizeformat
from django_read import DJANGO_READ_UPLOAD_CONTENT_TYPES, DJANGO_READ_UPLOAD_FILE_MAX_SIZE
from django_read.views import DocumentDetailView

class DocumentForm(forms.ModelForm):

    def clean_resource(self):
    	"""
    	This validation technique inspired by:
    	http://nemesisdesign.net/blog/coding/django-filefield-content-type-size-validation/
    	http://stackoverflow.com/questions/4853581/django-get-uploaded-file-type-mimetype
    	"""
        file = self.cleaned_data['resource']
        if hasattr(file, 'content_type'):
            content_type = file.content_type
            if len(file.name.split('.')) == 1:
                raise forms.ValidationError(_('File type is not supported'))
            if content_type in DJANGO_READ_UPLOAD_CONTENT_TYPES:
                if file._size > DJANGO_READ_UPLOAD_FILE_MAX_SIZE:
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
                        filesizeformat(settings.DJANGO_READ_UPLOAD_FILE_MAX_SIZE), filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_('File type is not supported'))
        return file

    def clean(self):
        cleaned_data = super(DocumentForm, self).clean()
        file = cleaned_data['resource']
        if hasattr(file, 'content_type'):
            cleaned_data['content_type'] = file.content_type
        return cleaned_data

    class Meta:
        fields = ['title', 'description', 'resource', 'parent']


class DocumentAdmin(DjangoMpttAdmin):
    list_display=['title', 'description']
    readonly_fields = ['content_type', 'extension']
    form = DocumentForm

    def save_model(self, request, obj, form, change):
        obj.content_type = form.cleaned_data.get('content_type', '')
        obj.save()

    def get_urls(self):
        urls = super(DocumentAdmin, self).get_urls()
        custom_urls = patterns('',
            (r'^view/(?P<pk>\d+)/$', DocumentDetailView.as_view())
        )
        return custom_urls + urls




admin.site.register(Document, DocumentAdmin)
