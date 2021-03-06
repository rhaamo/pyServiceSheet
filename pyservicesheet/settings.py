"""
Django settings for pyservicesheet project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import logging.config
import environ

logger = logging.getLogger("pyservicesheet.config")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = environ.Path(__file__) - 2  # (/a/b/myfile.py - 2 = /)
APPS_DIR = ROOT_DIR.path("controllers")
BASE_DIR = environ.Path(__file__) - 2

# Env loading for settings
env = environ.Env()
env_file = env("ENV_FILE", default=None)
if env_file:
    print(f"Loading specified env file at {env_file}")
    # we have an explicitely specified env file
    # so we try to load and it fail loudly if it does not exist
    env.read_env(env_file)
else:
    # we try to load from .env and config/.env
    # but do not crash if those files don't exist
    paths = [
        # /srv/pyservicesheet/api/.env
        ROOT_DIR,
        # /srv/pyservicesheet/.env
        (ROOT_DIR - 1),
    ]
    for path in paths:
        try:
            env_path = path.file(".env")
        except FileNotFoundError:
            print(f"No env file found at {path}/.env")
            continue
        env.read_env(env_path)
        print(f"Loaded env file at {path}/.env")
        break

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default=None)

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# Logging
# ------------------------------------------------------------------------------
LOGLEVEL = env("LOGLEVEL", default="info").upper()
LOGGING_CONFIG = None
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"console": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"}},
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "console"},
        },
        "loggers": {
            "pyservicesheet": {
                "level": LOGLEVEL,
                "handlers": ["console"],
                # required to avoid double logging with root logger
                "propagate": False,
            },
            "": {"level": LOGLEVEL, "handlers": ["console"]},
        },
    }
)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])
INTERNAL_IPS = ALLOWED_HOSTS

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "baton",  # has to be there
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "mptt",
    "imagekit",
    "django_admin_listfilter_dropdown",
    "django_extensions",
    "bootstrap4",
    "dynamic_preferences",
]

LOCAL_APPS = ["controllers.categories", "controllers.manufacturers", "controllers.items"]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + ["baton.autodiscover"]  # has to be at the end too

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pyservicesheet.urls"

WSGI_APPLICATION = "pyservicesheet.wsgi.application"


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# CONN_MAX_AGE seems to causes issues
# DATABASES["default"]["CONN_MAX_AGE"] = env("DB_CONN_MAX_AGE", default=60 * 5)


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = env("TIME_ZONE", default="UTC")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = env("LANGUAGE_CODE", default="en-us")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(APPS_DIR.path("templates"))],
        "OPTIONS": {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            "debug": DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                # Your stuff: custom template context processors go here
                "controllers.contexts.add_common_context",
                "dynamic_preferences.processors.global_preferences",
            ],
        },
    }
]

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = env("STATIC_ROOT", default=str(ROOT_DIR("static")))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
# STATICFILES_DIRS = (str(APPS_DIR.path("static")),)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = env("MEDIA_ROOT", default=str(APPS_DIR("media")))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"
FILE_UPLOAD_PERMISSIONS = 0o644

ATTACHMENTS_UNATTACHED_PRUNE_DELAY = env.int("ATTACHMENTS_UNATTACHED_PRUNE_DELAY", default=3600 * 24)

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = "pyservicesheet.urls"
ASGI_APPLICATION = "pyservicesheet.asgi.application"
WSGI_APPLICATION = "pyservicesheet.wsgi.application"
ADMIN_URL = env("DJANGO_ADMIN_URL", default="^admin/")

# This ensures that Django will be able to detect a secure connection
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Various other things
ITEM_ATTACHMENT_ALLOWED_PICTURES_TYPES = [
    "image/gif",
    "image/jpeg",
    "image/png",
]

ITEM_ATTACHMENT_ALLOWED_OTHER_TYPES = [
    "application/pdf",
    "application/xml",
    "image/svg+xml",
    "text/html",
    "text/plain",
    "text/xml",
    "application/msword",
    "application/vnd.ms-excel",
    "application/vnd.oasis.opendocument.text",
    "application/vnd.oasis.opendocument.spreadsheet",
    "application/zip",  # excel lol
]

# 50M (50*1024*1024)
FILE_UPLOAD_MAX_MEMORY_SIZE = env("FILE_UPLOAD_MAX_MEMORY_SIZE", default=50 * 1024 * 1024)
DATA_UPLOAD_MAX_MEMORY_SIZE = FILE_UPLOAD_MAX_MEMORY_SIZE

# Baton admin config
BATON = {
    "SITE_HEADER": "pyServiceSheet",
    "SITE_TITLE": "pyServiceSheet",
    "INDEX_TITLE": "Site administration",
    "SUPPORT_HREF": "https://github.com/rhaamo/pyServiceSheet",
    "COPYRIGHT": "squeak squeak",  # noqa
    "POWERED_BY": "an otter",
    "CONFIRM_UNSAVED_CHANGES": True,
    "SHOW_MULTIPART_UPLOADING": True,
    "ENABLE_IMAGES_PREVIEW": True,
    "CHANGELIST_FILTERS_IN_MODAL": False,
    "CHANGELIST_FILTERS_ALWAYS_OPEN": True,
    "MENU_ALWAYS_COLLAPSED": False,
    "MENU_TITLE": "Menu",
    "GRAVATAR_DEFAULT_IMG": "retro",
    "ANALYTICS": None,
}

if DEBUG:
    # Speed up a bit ImageKit
    # if DEBUG=True, all caching is disabled...
    IMAGEKIT_CACHE_BACKEND = "default"
    IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = "imagekit.cachefiles.strategies.Optimistic"
    IMAGEKIT_DEFAULT_CACHEFILE_BACKEND = "imagekit.cachefiles.backends.Simple"
else:
    IMAGEKIT_CACHE_BACKEND = "default"
    IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = "imagekit.cachefiles.strategies.Optimistic"
    IMAGEKIT_DEFAULT_CACHEFILE_BACKEND = "imagekit.cachefiles.backends.Simple"

SITE_URL = env("SITE_URL", default="http://localhost")
