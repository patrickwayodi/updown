"""
Views for the "uploads" Django app.
"""


import io
import json
import logging
import os
import subprocess

from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, View

from .forms import UploadForm
from .models import Upload


site_name = settings.SITE_NAME


class UploadCreateView(CreateView):

    model = Upload

    form_class = UploadForm

    template_name = "uploads/create_upload.html"


class UploadDetailView(DetailView):

    template_name = "uploads/upload_detail.html"

    model = Upload

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["upload"] = get_object_or_404(Upload, pk=self.kwargs["pk"])

        context["site_name"] = site_name

        return context


class UploadListView(ListView):

    model = Upload

    template_name = "uploads/upload_list.html"

    def get_queryset(self, **kwargs):

        queryset = Upload.objects.order_by("-id")[:50]

        return queryset

    def get_context_data(self, **kwargs):

        context = super(UploadListView, self).get_context_data(**kwargs)

        context["uploads"] = Upload.objects.order_by("-id")[:50]

        context["site_name"] = site_name

        return context

