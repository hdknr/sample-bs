# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from corekit import views as core_views
from . import models
from logging import getLogger

logger = getLogger()


class PostView(core_views.View):
    @core_views.handler(
        url=r'^(?P<id>\d+)$',
        name="blogs_post_detail", order=40,)
    def detail(self, request, id):
        instance = models.Post.objects.filter(id=id).first()
        if not instance:
            return self.page_not_found()

        return self.render(
            'blogs/post/detail.html', instance=instance)
