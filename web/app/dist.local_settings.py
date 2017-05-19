# coding :utf-8

from django.conf import global_settings
STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS + [
    'djangobower.finders.BowerFinder',
]
ALLOWED_HOSTS = ['develop.local', ]
