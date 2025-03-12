"""
This is the forms module for the "uploads" app.
"""


from django import forms

from .models import Upload


class UploadForm(forms.ModelForm):

    uploaded_file = forms.FileField(label = False)

    class Meta:

        model = Upload

        fields = ["uploaded_file",]

