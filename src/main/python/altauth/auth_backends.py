from django.contrib.auth.models import User, check_password

from altauth.models import AlternativePassword, PublicKeyLoginToken

"""
Alternative authentication backends

"""


def alternative_password_authenticate(username, alternative_password):
    """
    Login function for AlternativePasswordBackend
    """
    if username and alternative_password:
        try:
            user = User.objects.get(username=username)
            try:
                user_alternative_password = AlternativePassword.objects.get(user=user)
                if check_password(alternative_password,
                                  user_alternative_password.alternative_password):
                    return user
            except AlternativePassword.DoesNotExist:
                pass
        except User.DoesNotExist:
            pass
    return None


class AlternativePasswordBackend(object):
    """
    Tries to login against an alternative password
    """

    def authenticate(self, username=None, alternative_password=None):
        return alternative_password_authenticate(
            username,
            alternative_password)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def pubkey_authenticate(username, token, pubkey_type='RSA'):
    """
    Login function for PublicKeyBackend
    """
    if username and token and pubkey_type:
        try:
            user = User.objects.get(username=username)
            try:
                public_key_login_token = PublicKeyLoginToken.objects.get(
                    public_key__user=user,
                    public_key__pubkey_type=pubkey_type,
                )
                token_valid = public_key_login_token.check_token_is_valid(token)
                public_key_login_token.delete()
                if token_valid:
                    return user
            except PublicKeyLoginToken.DoesNotExist:
                pass
        except User.DoesNotExist:
            pass
    return None


class PublicKeyBackend(object):
    """
    Tries to login using a pubkey encrypted token
    """

    def authenticate(self, username=None, token=None):
        return pubkey_authenticate(
            username,
            token)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
