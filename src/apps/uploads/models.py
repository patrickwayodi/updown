"""
Models for the "uploads" app.
"""


import uuid

from django.db import models
from django.urls import reverse


class Upload(models.Model):

    uploaded_file = models.FileField(
        upload_to="uploadedfiles",
        verbose_name="File",
        blank=True,
        null=True,
    )

    date_uploaded = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # owner = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("upload_detail", args=[str(self.id)])

    def __str__(self):
        return self.uploaded_file.name

