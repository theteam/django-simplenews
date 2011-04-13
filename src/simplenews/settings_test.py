import os

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/simplenews.db'
INSTALLED_APPS = ['simplenews']
ROOT_URLCONF = 'simplenews.urls'

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
here = lambda *x: os.path.join(PROJECT_ROOT, *x)

TEMPLATE_LOADERS = (
    'django.template.loaders.eggs.load_template_source',
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)


TEMPLATE_DIRS = (
    here('tests', 'templates'),
)