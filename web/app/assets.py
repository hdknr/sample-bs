# coding: utf-8
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
ASSET_APPS = [
    'bootstrap3',               # django-bootstrap3
    'djangobower',              # django-bower
    'bambu_bootstrap',          # bambu
]

BOOTSTRAP3 = {
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components/')
# BOWER_PATH = '/usr/bin/bower'
BOWER_INSTALLED_APPS = [
    'jquery',
    'jquery-ui',
    'bootstrap',
    'fontawesome',
    'lightslider',      # https://github.com/sachinchoolur/lightslider.git
]
