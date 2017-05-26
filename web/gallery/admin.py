# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.contrib import admin
from corekit import admin as core_admin


class ImageFileAdmin(core_admin.CoreAdmin):
    raw_id_fields = ['user', ]


core_admin.register(__name__, globals(), [],)
