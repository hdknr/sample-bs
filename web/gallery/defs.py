# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import files


class ImageFile(models.Model):

    data = models.ImageField(
        _('Image File'),
        upload_to=files.ImageFilePath('public', 'data'))

    filename = models.CharField(
        _('Image File Name'), max_length=200,
        null=True, default=None, blank=True)

    key = models.CharField(
        _('Image File Key'), max_length=70,
        null=True, default=None, blank=True, unique=True)

    class Meta:
        abstract = True
