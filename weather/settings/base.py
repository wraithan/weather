from os.path import dirname, abspath, join

import dj_database_url


ROOT_DIR = dirname(dirname(abspath(__file__ + '/../')))

DATABASES = {
    'default': dj_database_url.config(default='postgresql://localhost/weather')
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (('Wrathan', 'xwraithanx@gmail.com'),)
MANAGERS = ADMINS

LANGUAGE_CODE = 'en-us'
MEDIA_ROOT = ''
MEDIA_URL = ''
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'weather.urls'
SECRET_KEY = 'g^_nwzr&t)n-!f&4lu2oum-yci=f8o2cc9^huq683wprp-55&o'
SITE_ID = 1
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_ROOT = join(ROOT_DIR, 'static/')
STATIC_URL = '/static/'
TEMPLATE_DIRS = ()
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'weather.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'gunicorn',
    'weather.core',
)

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
