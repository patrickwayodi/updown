"""
Models module for the Accounts app.
"""


from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):

    pass

    def __str__(self):

        return self.username

