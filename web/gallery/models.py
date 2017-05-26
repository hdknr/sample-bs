# coding: utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

from corekit.defs import CoreModel
from . import defs, methods


class ImageFile(defs.ImageFile, CoreModel, methods.ImageFile):
    '''画像'''

    user = models.ForeignKey(
        User, verbose_name=_('Image Owner'))

    class Meta:
        verbose_name = _('Image File')
        verbose_name_plural = _('Image Files')

    def __unicode__(self):
        return self.filename
