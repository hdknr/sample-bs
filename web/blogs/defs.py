# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(
        _('Post Title'), max_length=100)

    content = models.TextField(
        _('Post Content'), )

    class Meta:
        abstract = True
