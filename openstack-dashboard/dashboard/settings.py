import logging
import os
import sys

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

sys.path.append(ROOT_PATH)

SITE_ID = 1
SITE_BRANDING = 'OpenStack'
SITE_NAME = 'openstack'

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT =  os.path.join(ROOT_PATH, '..', 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

CREDENTIAL_AUTHORIZATION_DAYS = '5'

ROOT_URLCONF = 'dashboard.urls'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django_open.context_processors.enable_volumes'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'dashboard',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.comments',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.syndication',
    'django_nose',
    'django_open',
    'registration',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
TIME_ZONE = 'PST+08PDT,M3.2.0,M11.1.0'
LANGUAGE_CODE = 'en-us'
USE_I18N = False

ACCOUNT_ACTIVATION_DAYS = 7

try:
    from local.local_settings import *
except Exception, e:
    logging.exception(e)

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
