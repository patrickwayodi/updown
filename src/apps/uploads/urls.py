"""
URL configuration for the "uploads" Django app.
"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import UploadCreateView
from .views import UploadDetailView
from .views import UploadListView


urlpatterns = [
    path("upload/new/", UploadCreateView.as_view(), name="create_upload",),
    path("upload/<int:pk>/", UploadDetailView.as_view(), name="upload_detail",),
    path("uploads/", UploadListView.as_view(), name="upload_list",),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

