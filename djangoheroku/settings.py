"""
Django settings for djangoheroku project on Heroku. Fore more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "zxu_l$p+swpk7sg&(3&*@j0jai&+ov+@okh59x+r5v6tfhquin"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = (

    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local apps
    'backoffice',
    'frontoffice',

    # third party apps
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'djangoheroku.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoheroku.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# Internationalization and localization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Rome'  # 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (BASE_DIR + '/locale', )
LANGUAGES = (
    ('en', _('English')),
    ('it', _('Italian')),
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEFAULT_LOG_LEVEL = 'WARNING'

_HANDLERS = {
    'console': {
        'level': DEFAULT_LOG_LEVEL,
        'formatter': 'default',
        'class': 'logging.StreamHandler'
    },
}

LOG_FORMAT = '[%(levelname)s %(asctime)s %(name)s %(module)s: %(processName)s] %(message)s'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': LOG_FORMAT
        }
    },
    'handlers': _HANDLERS,
    'loggers': {
        'django': {
            'level': DEFAULT_LOG_LEVEL,
        },
        'custom': {
            'level': DEFAULT_LOG_LEVEL,
        },
    },
    'root': {
        'handlers': _HANDLERS.keys(),
        'level': DEFAULT_LOG_LEVEL,
    }
}


######################
# Url configurations #
######################
DOMAIN = "example.com"
DOMAIN_URL = "http://www." + DOMAIN
LOGIN_URL = "/login/"
PRIVACY_POLICY_URL = ""
FACEBOOK_APP_ID = "..."
EMAIL_ADDRESS_FOR_SUPPORT = "support@" + DOMAIN


######################
# Python Social Auth #
######################

LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
MIDDLEWARE_CLASSES += (
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.linkedin.LinkedinOAuth',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)


# LINKEDIN
SOCIAL_AUTH_LINKEDIN_KEY = 'XXX'
SOCIAL_AUTH_LINKEDIN_SECRET = 'XXX'
# Add email to requested authorizations.
SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress', ]
# Add the fields so they will be requested from linkedin.
SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = ['email-address', 'headline', ]
# Arrange to add the fields to UserSocialAuth.extra_data
SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address'),
                                   ('headline', 'headline')]

# FACEBOOK
SOCIAL_AUTH_FACEBOOK_KEY = 'XXX'
SOCIAL_AUTH_FACEBOOK_SECRET = 'XXX'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'public_profile']

# TWITTER
SOCIAL_AUTH_TWITTER_KEY = 'XXX'
SOCIAL_AUTH_TWITTER_SECRET = 'XXX'

# PYTHON-SOCIAL-AUTH PIPELINE
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',     # <--- avoid multiple mail account (NB: is not secure)
    'social.pipeline.user.create_user',
    'frontoffice.utils.create_user_profile',              # <--- eg: configure a UserProfile
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)


# Loading test/prod settings based on ENV settings
ENV = os.environ.get('ENV', 'local')
if ENV == 'prod':
    try:
        from production_settings import *
    except ImportError:
        pass
