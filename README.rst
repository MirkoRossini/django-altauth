==============
django-altauth
==============

Set of utilities to allow for alternative authentication methods 
specifically thought for access through static scripts

Why this app?
=============

This app was created to address a user case that recently came up at work:
I'm managing a web service that works as a wrapper around some data. Users
can log in through ldap, and usually use this data as input for a script,
and don't want to store their passwords in the scripts for obvious reasons.


Supported methods
=================

AlternativePassword
-------------------
Allows the users to create an alternative password to 
use to authenticate to the website. This is useful for users who don't want to
store their personal password in their scripts.

Flow:

1. Go to 'altauth/set_alternative_password/' to set the alternative password

2. Connect using the form at 'altauth/alternative_password_login/'

PublicKey
---------
Allows the users to authenticate using a public key (for now, only RSA is supported).

Flow:

1. Go to 'altauth/set_public_key/' to set the public key.

2. Go to 'altauth/get_public_key_token/' to get an encrypted token for a certain user

3. Decript the token and use it to connect to 'altauth/public_key_login/'

Check out "example/example.sh" for a basic script that shows how to authenticate with a public key.

 


Quick start
===========

1. Add "altauth" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'altauth',
      )

2. Include the altauth URLconf in your project urls.py like this::

      url(r'^altauth/', include('altauth.urls')),

3. Run `python manage.py syncdb` to create the altauth models.

4. Add the authentication methods you need to AUTHENTICATION_BACKEND in settings.py::
     AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                                'altauth.auth_backends.AlternativePasswordBackend',
                                'altauth.auth_backends.PublicKeyBackend') 

5. That's all!


