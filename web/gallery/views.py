# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from corekit import views as core_views
from . import models
from logging import getLogger
logger = getLogger()


class ImageFileView(core_views.View):
    @core_views.handler(
        url=r'^imagefile$',
        name="gallery_imagefile_index", order=40,)
    def detail(self, request):
        instances = models.ImageFile.objects.filter(
            user=request.user, id__lt=20)
        return self.render(
            'gallery/imagefile/index.html', instances=instances)
