from django.shortcuts import render
from django.views.generic import DetailView
from django_read.models import Document

class DocumentDetailView(DetailView):

    context_object_name = "document"
    model = Document
