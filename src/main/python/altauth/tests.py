"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from altauth.models import PublicKey
from altauth.utils import decrypt_token_rsa


TEST_RSA_PUBKEY = """-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAmttqzVLII9G93MsEXQCEPYzqXuSmpAX3OKAC7Sxjx3JwGDR8JmAc
4QTuJMX8I1aJZXXztpxgJFeVROEMI8w6wwGwmfouMaOWmZvZvw6FVkSfWGFISkh6
S9RICiJeW2znzhajfzF5FK1fzk3mOw3qz5id/BaD6MnQFyyzdL2oN6MS40xXptVE
5LVEfVFNhuo66SPbk6NpXAPLYaG5B3oOdRmrceR4HTTE3dDotRAu7MfX3LMMzKc/
BqmOHN2elQP+P6uZbV4Am4fu9AaMALFa7SjU7NSNvlbVi9cCAHcF+d+jJE2di5gA
4/eryL6d6kaxcm4vqnW2tOXD8MO0M4995QIDAQAB
-----END RSA PUBLIC KEY-----
"""
TEST_RSA_PRIVKEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEqAIBAAKCAQEAmttqzVLII9G93MsEXQCEPYzqXuSmpAX3OKAC7Sxjx3JwGDR8
JmAc4QTuJMX8I1aJZXXztpxgJFeVROEMI8w6wwGwmfouMaOWmZvZvw6FVkSfWGFI
Skh6S9RICiJeW2znzhajfzF5FK1fzk3mOw3qz5id/BaD6MnQFyyzdL2oN6MS40xX
ptVE5LVEfVFNhuo66SPbk6NpXAPLYaG5B3oOdRmrceR4HTTE3dDotRAu7MfX3LMM
zKc/BqmOHN2elQP+P6uZbV4Am4fu9AaMALFa7SjU7NSNvlbVi9cCAHcF+d+jJE2d
i5gA4/eryL6d6kaxcm4vqnW2tOXD8MO0M4995QIDAQABAoIBAFlNCQUIpPPLAyMt
TAHZx2i7N3irgNF7wzo7RBTDkXK1sqCyu5lhuaWlszMvnRw/zhHdeEKpYOP0Qdcr
tFV8c7J66f2RgUwM208PyfzcgdXi0sUjrI1xyFysOTLm6OTuI6r78SLrQ7jB1krh
L1CE0REQIKL71OvMXThZHUedWlAExk9/Jwkbdnseyi7ClIQBu2Z7ShTTL17RbGSV
UFWdmiratXHilmNSqUOri/pIpw7417xDg0IVfknhCp/4dapGn8qakCj6Rvsr1dzZ
QKYgYhemkfv9Hfl7+tO96OtUu/GpnDkog5JTuHNzIz/Tfwq9h6iOrezjHaoiZATA
pIoJHiECgYkArjaWHuuHhJmDiIpdrbY6U2GAaEb8gHaM8ptqHMwLi0455qHXIsZ7
RToEKzJqeloBWo7ZWjqC9uo9LakmMwAZVRKs58uTkXnXCsUTb74jZn1gGx+9WNyw
sShe1I4s+RAPtIXWdQIkGKCGskBLRh9yDHdY5fexUrrCFKICE58RlCP3kOhlPNJa
mQJ5AOOOjyN6pVeC9jyukAY0n8bywhQRlncWP8CL31I8ogqW0T0XJw1J4RIoKokt
BBckSf1Shm+jZc+mukCycXBd7PFaSQGYEfmbg8rNXSnF0vB8nmtfi43Cq6mYWHgq
WRestn0kZCFQWqIdx4wDkV8sPfjHnkkn/yW5LQKBiDT/VCHp4tsa3GHQPflXg1zU
P3z5g10NM4mmb9x80lI5pPGdcFYa7Ws84AHIH45DDUBgTozdWfQFhED8wSsor4wq
10DYtHbACwQyudv3istl/rOhrzd2Q6ZRMrAU5GeMVErFoF0OHq8DPpbBamTVshtK
v1eOR3p0aBBgzKLtdCqN2oVRvWKIV5kCeF5fxWWFfAUrP0wzaW/pa0pra6o/ERQa
mh4U5G2Kz/lsSyL28y9DsKCDIAD8NnISjs0M6MxsC9Fu6Ffkqb9cdOQz+Ys7sli+
8o2tVjH45V7vkBQf8BS+48rWb/qGNaTn8Fc+PHjEhpItn5Cl+ihqhNkkkLTubZcL
kQKBiDoeEQhAzKOPivh8zL4K0zUYD3JYYbOaJ1OsBDBHvPdVhqkLwiITDFHGot3t
C1rNTk4vyG6akiucwp/qoCb9pyJ/7ZLr9rmu6cCOOk9LQfXhJdR6QsisaYBO9Jle
d9RZu7YNZoqS5p2OUQp+7DlzODApcXMo2TyZzE26zHdiTPGpTqSIR1HvGcQ=
-----END RSA PRIVATE KEY-----
"""


class AltAuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='user', password='test')

        self.rsa_pubkey = TEST_RSA_PUBKEY
        self.rsa_privkey = TEST_RSA_PRIVKEY

        # Uncomment to use with your own public/private keys
        # we use ssh format for pubkey to test the "converter"
        # self.rsa_pubkey = open(os.path.expanduser('~') + '/.ssh/id_rsa.pub').read()
        # self.rsa_privkey = open(os.path.expanduser('~') + '/.ssh/id_rsa').read()

    def test_alternative_password_creation(self):
        """
        Tests that the form to create an alternative password works.
        Also tries to log in with the alternative password
        """

        # Test the set
        self.client.logout()
        response = self.client.get(reverse('altauth_set_alternative_password'))
        self.assertEqual(response.status_code, 302)  # Login is required
        self.client.login(username='user', password='test')

        response = self.client.post(
            reverse('altauth_set_alternative_password'),
            {})
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('altauth_set_alternative_password'),
                                    {'passphrase': 'alternative password'})
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('altauth_set_alternative_password'),
                                    {'passphrase': 'alternative password', 'salt': 'salt'})

        self.assertEqual(response.status_code, 200)

        self.client.logout()

        # Test if the alternative password login method works
        response = self.client.post(reverse('altauth_alternative_password_login'),
                                    {'username': 'user',
                                     'alternative_password': 'wrong pwd'})
        self.assertNotIn('_auth_user_id', self.client.session)  # not authorized, so not logged in

        response = self.client.post(reverse('altauth_alternative_password_login'),
                                    {'username': 'user',
                                     'alternative_password': 'alternative password'})
        self.assertEqual(response.status_code, 302)  # redirect after login

        response = self.client.get(reverse('altauth_set_alternative_password'))
        self.assertEqual(response.status_code, 200)  # As a logged in user I can see the form

    def test_rsa_pubkey_login(self):
        """
        tests the following flow:
        - set rsa public key
        - generate a login token
        - decrypt the token
        - use token to log in
        """
        self.client.logout()

        # Save the public key
        response = self.client.get(reverse('altauth_set_public_key'))
        self.assertEqual(response.status_code, 302)  # Login is required
        self.client.login(username='user', password='test')
        response = self.client.post(reverse('altauth_set_public_key'),
                                    {'public_key': self.rsa_pubkey,
                                     'pubkey_type': 'RSA'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'successful')

        user = User.objects.get(username='user')

        self.assertTrue(PublicKey.objects.get(
            user=user,
            pubkey_type='RSA').public_key not in (None, '')
        )

        # Generate a login token
        response = self.client.post(
            reverse(
                'altauth_get_public_key_token'),
            {'username': 'user', })
        token = decrypt_token_rsa(response.content, self.rsa_privkey)

        # Authentication with encrypted token
        response = self.client.post(
            reverse('altauth_public_key_login'),
            {'username': 'user',
             'token': token})

        # user is logged in
        self.assertIn('_auth_user_id', self.client.session)

        self.client.logout()
        # test token is valid only once
        response = self.client.post(
            reverse('altauth_public_key_login'),
            {'username': 'user',
             'token': token})

        # user is not logged in
        self.assertNotIn('_auth_user_id', self.client.session)
