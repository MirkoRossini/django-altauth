# Django settings for example project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/tmp/altauth_test.sqlite3db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h32z)k0^nx9b+s(ec9*u05=%esmk!+r_%nz_*034iep@@b5+2k'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'example.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'example.wsgi.application'

TEMPLATE_DIRS = (
    os.path.dirname(__file__) + '/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'altauth',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

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

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'altauth.auth_backends.AlternativePasswordBackend',
                           'altauth.auth_backends.PublicKeyBackend',
                            )



ALTAUTH_RSA_PUBLIC_KEY = """-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAgOcQ7euSkdnbf11flsrwrt6ak4Vloz7sflFPLj0cLxXMqAEZ+IhJ
IQZXTObxFZMt697KS6D+lY4gmDQdv9xW1yx1DFpHkLuKeUXvc7mK7kf6kQP2jTe6
Z7t3fgQK7RrlHulSyIwfpWLVeOHptptsNxSFm6mbBZi+f/ZuCBrNWYaGdmtu0Mlu
r4HlksG22NHXjRwaAA30m3mSsz8O/KMnhVnYXRpzmFqZ93Bf67Zy1eqeygTQKchQ
GfZw7s176vdXNrDW6J1jt/S4q4sWwTIGePs0aOdvBwJdibub4dd2TgKsbEWbHmpQ
2g68ZvkQ8DxRMoLbw+cWouepgeVGvZ/+/QIDAQAB
-----END RSA PUBLIC KEY-----"""

ALTAUTH_RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEqAIBAAKCAQEAgOcQ7euSkdnbf11flsrwrt6ak4Vloz7sflFPLj0cLxXMqAEZ
+IhJIQZXTObxFZMt697KS6D+lY4gmDQdv9xW1yx1DFpHkLuKeUXvc7mK7kf6kQP2
jTe6Z7t3fgQK7RrlHulSyIwfpWLVeOHptptsNxSFm6mbBZi+f/ZuCBrNWYaGdmtu
0Mlur4HlksG22NHXjRwaAA30m3mSsz8O/KMnhVnYXRpzmFqZ93Bf67Zy1eqeygTQ
KchQGfZw7s176vdXNrDW6J1jt/S4q4sWwTIGePs0aOdvBwJdibub4dd2TgKsbEWb
HmpQ2g68ZvkQ8DxRMoLbw+cWouepgeVGvZ/+/QIDAQABAoIBAFmhUfI9tYLZG3kq
cgcmQck2XAFr5kpmvIbw/r/GGkzbOZ0wduCL0121TQraIpS/7FRwa/W+kodndl6f
DniUO4YPEaxvMgf/f7/n0yKCx4n8XsxrFwsGzwTGI8ZqBTbtVpfx4XA1juOvH4SY
gaxJ0itSh7y/aF2x4VTTKKpTAMo0ii1nrqYALveVHtLp5F4A8e+jh46apIX87/xe
17y3qO7E0J5BDPx89MBa/UCeRRwRspwftFU35rHQqdls49HBc6txdsDuicM+ZaDl
RujvmLcmHHS8nxB+BnMMXygLPSseTSwAZoWSVdg1TsExq3ICROlUkid8spr9g2bo
07slDLkCgYkA5cDOSeyEW3v2NfZtLU5jKxkEagu7rUmltIWT3u/KbVf6OWXmPC7n
WN1S98qF6KIwi+xFpupdA0hj3g4dAZkkJrL3sKXn6Gr3O0KUn7+Cyg2Hkk0KMpq+
0ztL379HACJA7U02tkhdkaFWald//8hxRxfMiWoH4j/b/N1YjkhlK83XXCIV8XaZ
awJ5AI+g27ixYymjLMRegErUpB4rP6qZTMQUokqpWr3TqAv/JcpK8WYonijZguNL
Kubk+jjQIymx1iN+wEUGD3I9L1ZoH2TygxJdxvIfMQf05jU0MDIGofS/jtiK5wMo
gzI1FYlixIj0EY+GXkyhtqHFbrIxq0Ws+NRbNwKBiG4EE0QGw6JjC5TveXwWaxo6
EokNMUNbXsPAqvw36sDNPf66MrNi6lj9MjuBePnaoFCARSIWW4+03E16iJ05TbxS
OpUV/KSog9aWnUCZnfFO5TpDNbzhqLrRTBXKLB9+R4TaUnaa1GNl1FF7sMk0nDmk
xcaPRVMrrRW6kCshs4B0QsnVcJh9aB0CeDY/+f4O8nedrKEXWLnrC3pht5CGitpd
ONeelCmzMnwliW6ZVAjUOrkPP0L+91tzDZg79awgAdQyYgkwOtFZjvHCLmmAuEVN
qoF1ip2IwRNDfRjILJA3cosUHCGzQarLJjFYXwejuKZPiHrFcig0XJVt8VVF+k6r
jQKBiEuTCt89ZzyqQ6XBHLBhmeRU+jiTdfmJWK2nG/sxLh1lFxYiH3uQaElK7nEK
biZbzZXwdfF11Zdo9mj9fszm8s3xnXDzasreYewDgCQtXWGmqb6c9kZa7O+MLb99
3tV0SzmmuegDkxV9KPeYBD6Qyrp5VDWoBLbIMA3d9UKUjNc4s2wIWQ3AnRA=
-----END RSA PRIVATE KEY-----
"""

# Alternatively, you can simply use: open(os.path.expanduser('~') + '.ssh/id_rsa').read()

#ALTAUTH_RSA_PUBLIC_KEY = open(os.path.expanduser('~') + '/.ssh/id_rsa.pub').read()
#ALTAUTH_RSA_PRIVATE_KEY = open(os.path.expanduser('~') + '/.ssh/id_rsa').read()

