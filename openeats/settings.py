# Django settings for openeats project.
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
SERVE_MEDIA = True

ADMINS = (
    # ('Your Name', 'youremail@email.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_PATH, 'db.sqlite3'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.

TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

ugettext = lambda s: s

LANGUAGES = (
     ('en', ugettext('English')),
     ('de', ugettext('German')),
     ('es', ugettext('Spanish')),
   )

SITE_ID = 1


CACHE_BACKEND = "file://"+os.path.join(BASE_PATH, 'cache')

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_PATH, 'site-media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site-media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_PATH, 'static')

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tk1ig_pa_p9^muz4vw4%#q@0no$=ce1*b$#s343jouyq9lj)k33j('

INCLUDE_REGISTER_URL = True
INCLUDE_AUTH_URLS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_PATH, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                'django.template.context_processors.static',
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "openeats.context_processors.oelogo",
                "openeats.context_processors.oetitle",
            ],
            'debug': True,
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware'
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

LOCALE_PATHS = (
    os.path.join(BASE_PATH, 'locale'),
)

ROOT_URLCONF = 'openeats.urls'

INSTALLED_APPS = (
    #'grappelli.dashboard',
    #'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    #'taggit',
    #'taggit_templatetags',
    #'registration',
    #'profiles',
    #'imagekit',
    #'djangoratings',
    #'haystack',
    'pagination',
    'django_extensions',
    #'relationships',
    'tastypie',
    'recipe',
    'recipe_groups',
    'ingredient',
    'openeats',
)


#OpenEats2 Settings
OELOGO = 'images/oelogo.png'
OETITLE = 'OpenEats2 Dev'

#Email Server Settings
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT =''
#EMAIL_USE_TLS = True

#registration
LOGIN_REDIRECT_URL = "/recipe/"
ACCOUNT_ACTIVATION_DAYS = 7

#Haystack config
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH':    os.path.join(BASE_PATH, 'search_index')
    }
}



PAGINATION_DEFAULT_PAGINATION = 10


try:
    from local_settings import *
except ImportError:
    pass
