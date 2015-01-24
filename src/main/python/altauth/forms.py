from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from altauth.models import ALLOWED_PUBLICKEY_TYPES


class SetAlternativePasswordForm(forms.Form):
    """
    Form to store an alternative password for a user
    """
    passphrase = forms.CharField(max_length=128, required=False)
    salt = forms.CharField(max_length=128, required=False)


class SetPublicKeyForm(forms.Form):
    """
    Form to store a public key for the user
    """
    public_key = forms.CharField(widget=forms.Textarea, max_length=500, required=True)
    pubkey_type = forms.ChoiceField(choices=ALLOWED_PUBLICKEY_TYPES, required=False, initial='RSA')


class AltauthLoginForm(forms.Form):
    username = forms.CharField(max_length=254)
    error_messages = AuthenticationForm.error_messages

    def __init__(self, *args, **kwargs):
        """
        This form works exactly like the AuthenticationForm in
        django.contrib.auth
        """
        self.user_cache = None
        super(AltauthLoginForm, self).__init__(*args, **kwargs)

    def custom_validation(self, message='Could not validate user'):
        if self.user_cache is None:
            raise forms.ValidationError(
                message
            )
        elif not self.user_cache.is_active:
            raise forms.ValidationError(self.error_messages['inactive'])


class PublicKeyLoginForm(AltauthLoginForm):
    """
    Form to log in using a public key encrypted token
    """
    token = forms.CharField(max_length=254)

    def clean(self):
        username = self.cleaned_data.get('username')
        token = self.cleaned_data.get('token')
        if username and token:
            self.user_cache = authenticate(username=username,
                                           token=token)
            self.custom_validation("dio porco")
        return self.cleaned_data


class AlternativePasswordLoginForm(AltauthLoginForm):
    """
    Form to log in against the alternative password
    """
    alternative_password = forms.CharField(max_length=128)

    def clean(self):
        username = self.cleaned_data.get('username')
        alternative_password = self.cleaned_data.get('alternative_password')

        if username and alternative_password:
            self.user_cache = authenticate(username=username,
                                           alternative_password=alternative_password)
            self.custom_validation()
        return self.cleaned_data
