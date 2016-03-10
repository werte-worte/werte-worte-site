import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for werteworte project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Use this value to (prefix-)match when you want to differentiate dev/test/production
CONFIGURATION = os.environ.get('DJANGO_CONFIGURATION', 'development').lower()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Hence, this value must be overwritten in a local settings split file (e.g. 90-local.py)
SECRET_KEY = 'x^c-1@1zih=u32$5^r$ptr@!p^oliwdg1kpb#6)^*^d5s-38sk'

# SECURITY WARNING: don't run with debug turned on in production!

if not CONFIGURATION.startswith("prod"):
    DEBUG = True

ALLOWED_HOSTS = ('*', )


# Application definition





ROOT_URLCONF = 'werteworte.urls'

WSGI_APPLICATION = 'werteworte.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'werteworte', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'werteworte', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

if not CONFIGURATION.startswith("prod"):
    TEMPLATES[0]['OPTIONS']['debug']='true'

MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'bootstrapform',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'newsletter',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'cmsplugin_iframe',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'djangocms_newsletter_subscription',
    'reversion',
    'werteworte'
)

if CONFIGURATION.startswith("dev"):
    INSTALLED_APPS += ('debug_toolbar',)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LANGUAGES = (
    ## Customize this
    ('de', gettext('de')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'name': gettext('de'),
            'redirect_on_fallback': True,
            'public': True,
            'code': 'de',
            'hide_untranslated': False,
        },
    ],
    'default': {
        'public': True,
        'redirect_on_fallback': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

# One will typically overwrite this in a local settings split file for Postgres config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

# comment this if you do not have MemCache on your production machine
if CONFIGURATION.startswith('prod'):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'TIMEOUT': 6000,
            # Chose a unique KEY_PREFIX to avoid clashes with other applications
            # using the same cache (e.g. a shared memcache instance).
            'KEY_PREFIX': 'wworte_' + CONFIGURATION[:4],
        }
    }

MIGRATION_MODULES = {
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django'
}


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
#   ('default', 'Default'),
#   ('width-80', 'Scale to 80% of width'),
# )
