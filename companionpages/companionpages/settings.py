import imp
import sys

from os import environ as env
from os.path import abspath, dirname, join, normpath
import dj_database_url


DJANGO_ROOT = dirname(abspath(__file__))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_TITLE = 'RunMyCode'

sys.path.append(DJANGO_ROOT)

DEBUG = True if env.get('DEBUG', False) == 'True' else False
TEMPLATE_DEBUG = DEBUG

# heroku suggested setting
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ADMINS = [(admin.split('@')[0], admin) for admin in env.get('ADMINS', 'tyler@starkravingsane.org').split(',')]
MANAGERS = ADMINS

# dj_database_url will pull from the DATABASE_URL environment variable
DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost:5432/tyler'),
        #'default': dj_database_url.config(default='sqlite:////' + SITE_ROOT + '/tyler.db'),
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = env.get('SITE_ID', 1)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# email settings

# default to console for backend
EMAIL_BACKEND = env.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')

# django-envelope contact page settings
DEFAULT_FROM_EMAIL = env.get('DEFAULT_FROM_EMAIL', 'devtyler@codersquid.com')
ENVELOPE_CONTACT_CHOICES = (
    ('',    u"Choose"),
    (10,    u"A question regarding the website"),
    (20,    u"A question regarding companion pages"),
    (None,   u"Other"),
)
MAILGUN_ACCESS_KEY = env.get('MAILGUN_ACCESS_KEY')
MAILGUN_SERVER_NAME = env.get('MAILGUN_SERVER_NAME')

# spam catching
HONEYPOT_FIELD_NAME = 'relatedtopics2'

# s3 amazon static file storage settings
AWS_STORAGE_BUCKET_NAME = env.get('AWS_STORAGE_BUCKET_NAME', 'starkravingsanermccompanion')
S3_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
# WORKAROUND
# I'm using strip("'") because heroku is inserting single quotes in heroku config settings
AWS_ACCESS_KEY_ID = env.get('AWS_ACCESS_KEY_ID', '').strip("'")
AWS_SECRET_ACCESS_KEY= env.get('AWS_SECRET_ACCESS_KEY', '').strip("'")
AWS_HEADERS = {}
DEFAULT_FILE_STORAGE = env.get('DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage')
# allow collectstatic automatically put your static files in your bucket
STATICFILES_STORAGE = env.get('STATICFILES_STORAGE', 'django.contrib.staticfiles.storage.StaticFilesStorage')

#from S3 import CallingFormat
#AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

# REST_FRAMEWORK = { }

# django-registration settings
ACCOUNT_ACTIVATION_DAYS = 2

# django-profiles
AUTH_PROFILE_MODULE = 'members.Member'


# django-gravatar
GRAVATAR_DEFAULT_SIZE = 80
#GRAVATAR_DEFAULT_IMAGE = 'https://s3.amazonaws.com/starkravingsanermccompanion/img/avatar_small.png'
GRAVATAR_DEFAULT_IMAGE = 'http://raw.github.com/codersquid/tyler/master/companionpages/static/img/avatar_small.png'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = normpath(join(SITE_ROOT, 'staticfiles'))
# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = S3_URL

#STATIC_URL = '/static/'
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
# URL that handles the media served from MEDIA_ROOT. Make sure to use a trailing slash.
#MEDIA_URL = '/media/'
MEDIA_URL = STATIC_URL + 'media/'
# Additional locations of static files
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
ADMIN_MEDIA_PREFIX = join(STATIC_URL, "admin/")



# Make this unique, and don't share it with anybody.
SECRET_KEY = env.get('SECRET_KEY')

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
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'companionpages.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'companionpages.wsgi.application'

TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',
    'django.contrib.flatpages',
)

THIRD_PARTY_APPS = (
    'envelope',
    'gunicorn',
    'honeypot',
    'profiles',
    'registration',
    'south',
    'storages',
    'gravatar',
    'taggit',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'home',
    'members',
    'news',
    'supportingmaterials',
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

if DEBUG:
    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    INSTALLED_APPS += (
        'debug_toolbar',
        'django.contrib.webdesign',
        'django.contrib.admindocs',
        'django_extensions',
    )
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    TEMPLATE_STRING_IF_INVALID = 'template_error'
    # use local files for static rather than amazon s3
    STATIC_URL = '/static/'
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS':False,
    }



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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


if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'NAME': ':memory:',
            #'ENGINE': 'django.db.backends.postgresql_psycopg2'
            'ENGINE': 'django.db.backends.sqlite3'
        }
    }
    imp.find_module('django_nose')
    INSTALLED_APPS = tuple(list(INSTALLED_APPS) + ['django_nose'])
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    SECRET_KEY = 'companionpages-test'
