from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("apps.accounts.urls")),
    path("", include('apps.pages.urls')),
    path("", include('apps.uploads.urls')),
    path("admin/", admin.site.urls),
]

