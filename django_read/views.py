from django.shortcuts import render
from django.views.generic import DetailView
from django_read.models import Document
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

class DocumentDetailView(DetailView):

    context_object_name = "document"
    model = Document
    template_name = "django_read/document_detail/default.html"

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(DocumentDetailView, self).dispatch(*args, **kwargs)

    def get_template_names(self):
    	object = self.get_object()
        if object.extension == ".epub":
        	return "django_read/document_detail/epub.html"
        else:
            return [self.template_name]