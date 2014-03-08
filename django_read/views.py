from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.detail import BaseDetailView
from django_read.models import Document
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django_read import DJANGO_READ_MEDIA_URL, DJANGO_READ_PRIVATE
from django.conf import settings

class DocumentDetailView(DetailView):

    context_object_name = "document"
    model = Document
    http_method_names = ['get']
    template_name = "django_read/document_detail/default.html"

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(DocumentDetailView, self).dispatch(*args, **kwargs)

    def get_template_names(self):
    	document = self.get_object()
        if document.extension == ".epub":
        	return "django_read/document_detail/epub.html"
        else:
            return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        if DJANGO_READ_PRIVATE:
        	resource_url = reverse("document_content_view", args=[str(self.object.pk)])
        else:
        	resource_url = "%s" % ( self.object.resource.url)
        context["resource_url"] = resource_url 
        return context


class DocumentContentView(BaseDetailView):

    model = Document
    http_method_names = ['get']
    
    @method_decorator(staff_member_required)
    def get_context_data(self, **kwargs):
        return super(DocumentContentView, self).get_context_data(**context)

    def get(self, request,  *args, **kwargs):
        document = self.get_object()
        response = HttpResponse()
        response["Content-Disposition"] = "attachment; filename={0}{1}".format(
            document.title, document.extension)
        response['Content-Type']=document.content_type
        response['X-Accel-Redirect'] = "{0}{1}".format(DJANGO_READ_MEDIA_URL, document.resource.name)
        return response
