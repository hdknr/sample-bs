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


class Review(models.Model):
    nickname = models.CharField(
        _('Nickname'), default=_('Default Nickname'), max_length=50)
    rating = models.PositiveIntegerField(
        _('Review Rating'), default=3,
        choices=tuple((j, j) for i, j in enumerate(range(1, 6))))
    text = models.TextField(_('Review Text'))

    class Meta:
        abstract = True
