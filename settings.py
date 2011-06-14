# coding=utf-8
import os.path
import sys
import platform

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
PRODUCTION_HOSTNAME = "tango"

ADMINS = (
    ('Johan Bichel Lindegaard', 'sysadmin@tango.johan.cc'),
)
MANAGERS = ADMINS

DEVELOPMENT_MODE = (platform.node() != PRODUCTION_HOSTNAME)

if DEVELOPMENT_MODE:
    DEBUG = True
    MEDIA_URL = '/m/'
    STATIC_URL = '/static/'
else:
    DEBUG = False
    MEDIA_URL = 'http://media.wetart.dk/'
    STATIC_URL = 'http://static.wetart.dk/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

TEMPLATE_DEBUG = DEBUG

# Static files
MEDIA_ROOT = BASE_PATH + '/media'
STATICFILES_DIRS = (
    BASE_PATH + '/static',
)

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'en'

SITE_ID = 1
USE_I18N = True
USE_L10N = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    BASE_PATH + '/templates/'
)

INSTALLED_APPS = (
    'profiles',
    'projects',

    'south',
    'sorl.thumbnail',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    execfile(BASE_PATH + '/settings_local.py')
except IOError:
    sys.stderr.write("\nYou need to copy settings_local.example to settings_local.py and customize it.\n")
    sys.exit(1)
