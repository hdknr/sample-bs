# coding: utf-8
from __future__ import unicode_literals
from django.utils.deconstruct import deconstructible
from django.utils import timezone

from corekit.files import UploadPath
import os
from logging import getLogger
logger = getLogger()


@deconstructible
class ImageFilePath(UploadPath):

    def generate_key(self, id, exts):
        return timezone.localtime(timezone.now()).strftime(
            '{}/%Y%m%d/%H%M%S.%f{}'.format(id, exts))

    def create_name(self, instance, filename):
        if filename:
            instance.filename = instance.filename or filename
            ext = os.path.splitext(filename)[1]     # starts with "."(dot)
            instance.key = instance.key or \
                self.generate_key(instance.user.id, ext)
            return instance.key
