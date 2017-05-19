# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    writer = models.ForeignKey(
        User, verbose_name=_('Post Writer'),
        null=True, blank=True, default=None, on_delete=models.SET_NULL)

    title = models.CharField(
        _('Post Title'), max_length=100)

    content = models.TextField(
        _('Post Content'), )

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
