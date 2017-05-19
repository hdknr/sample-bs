# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from corekit.defs import CoreModel
from . import defs, methods


class Post(CoreModel, defs.Post, methods.Post):
    writer = models.ForeignKey(
        User, verbose_name=_('Post Writer'),
        null=True, blank=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class Review(CoreModel, defs.Review, methods.Review):
    post = models.ForeignKey(
        Post, verbose_name=_('Post'))
    reviewer = models.ForeignKey(
        User, verbose_name=_('Reviewer'),
        null=True, blank=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
