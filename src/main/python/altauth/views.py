from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, make_password
from django.contrib.auth import login
from django.conf import settings

from altauth.models import AlternativePassword, PublicKey
from altauth.forms import (SetAlternativePasswordForm,
                           AlternativePasswordLoginForm, SetPublicKeyForm,
                           PublicKeyLoginForm)

from django.http import (HttpResponseRedirect, HttpResponse,
                         HttpResponseForbidden)
from django.utils.translation import ugettext_lazy as _


@login_required
def set_alternative_password(request):
    """
    View to set the alternative password on a user
    """
    context = {}
    if request.method == 'POST':
        form = SetAlternativePasswordForm(request.POST)
        if form.is_valid():
            form.cleaned_data['passphrase'] = \
                form.cleaned_data['passphrase'] or \
                get_random_string(100)
            passphrase = form.cleaned_data['passphrase']
            salt = form.cleaned_data['salt'] or None
            alternative_password = make_password(passphrase, salt)
            ap_entry, created = AlternativePassword.objects.get_or_create(
                user=request.user,
            )
            ap_entry.alternative_password = alternative_password
            ap_entry.save()
            context['alternative_password'] = passphrase
    else:
        form = SetAlternativePasswordForm()  # An unbound form

    context['form'] = form

    return render(request, 'altauth/set_alternative_password.html', context)


def alternative_password_login(request):
    """
    This view can be used to log in with the alternative
    password.
    """
    context = {}
    if request.method == 'POST':
        form = AlternativePasswordLoginForm(request.POST)
        if form.is_valid():
            user = form.user_cache
            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect_to = settings.LOGIN_REDIRECT_URL
                    return HttpResponseRedirect(redirect_to)

    else:
        form = AlternativePasswordLoginForm()

    context['form'] = form
    return render(request, 'altauth/alternative_password_login.html', context)


@login_required
def set_public_key(request):
    """
    View to set the alternative password on a user
    """
    context = {}
    if request.method == 'POST':
        form = SetPublicKeyForm(request.POST)
        if form.is_valid():
            pb_entry, created = PublicKey.objects.get_or_create(
                user=request.user,
                pubkey_type=form.cleaned_data['pubkey_type'],
            )
            pb_entry.public_key = form.cleaned_data['public_key']
            pb_entry.save()
            context['success'] = True
    else:
        form = SetPublicKeyForm()  # An unbound form

    context['form'] = form
    return render(request, 'altauth/set_public_key.html', context)


def get_public_key_token(request, pubkey_type='RSA'):
    """
    Returns a pubkey encripted token to allow log in through pubkey
    authentication.
    The returned value is a text/plain content encripted with the user's public key:
    <2-digits token length > <token> <server public key>
    """
    if request.method == 'POST' and request.POST['username']:
        try:
            user = User.objects.get(username=request.POST['username'])
            public_key = PublicKey.objects.get(user=user,
                                               pubkey_type=pubkey_type)
        except PublicKey.DoesNotExist:
            return HttpResponseForbidden(
                _(('no public key available for '
                   'pubkey type %(pubkey_type)s')) %
                {'pubkey_type': pubkey_type}
            )
        except User.DoesNotExist:
            return HttpResponseForbidden(_("Invalid username: %(username)s") %
                                         {'username': request.POST['username']})

        login_token = public_key.generate_login_token()
        return HttpResponse(login_token, content_type='text/plain')
    else:
        return HttpResponseForbidden(_("username not specified"))


def public_key_login(request):
    """
    This view can be used to log in with a public key.
    """
    context = {}
    if request.method == 'POST':
        form = PublicKeyLoginForm(request.POST)
        if form.is_valid():
            user = form.user_cache
            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect_to = settings.LOGIN_REDIRECT_URL
                    return HttpResponseRedirect(redirect_to)

    else:
        form = AlternativePasswordLoginForm()

    context['form'] = form
    return render(request, 'altauth/public_key_login.html', context)
