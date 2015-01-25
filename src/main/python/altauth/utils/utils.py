import rsa
from base64 import b64decode
from altauth.common import b


def hex_string_to_int(hexstring, pos=0, length=4, shift=8):
    """
    Converts a hex string to an integer
    """
    total = 0
    shift_multiplier = length
    for i in range(pos, pos + length):
        shift_multiplier -= 1
        total += (ord(hexstring[i]) << shift * shift_multiplier)
    return total


def get_rsa_public_key_from_ssh_public_key(ssh_public_key):
    """
    Takes as argument a string containing an rsa public key
    in the ssh format and returns a rsa.PublicKey instance

    Alternatively, one can use ssh-keygen convert tool:

    ssh-keygen -f ~/.ssh/id_rsa.pub -e -m pem > /tmp/a.pub
    """
    # Separate the key from the rest
    ssh_public_key = ssh_public_key.split()[1]
    ssh_public_key = b64decode(ssh_public_key)
    tlen = hex_string_to_int(ssh_public_key)
    endt = 4 + tlen
    elen = hex_string_to_int(ssh_public_key, endt)
    e = hex_string_to_int(ssh_public_key, endt + 4, elen)
    nlen = hex_string_to_int(ssh_public_key, endt + 4 + elen)
    n = hex_string_to_int(ssh_public_key, endt + 4 + elen + 4, nlen)
    return rsa.PublicKey(e=e, n=n)


def decrypt_token_rsa(encrypted_message, private_key):
    """
    decripts a token generated from the generate_login_token
    view
    """
    private_key = rsa.PrivateKey.load_pkcs1(
        b(private_key))
    token = rsa.decrypt(
        b(encrypted_message),
        private_key)
    return token


def decrypt_token_rsa_using_file(encrypted_message, private_key_path):
    """
    decripts a token generated from the generate_login_token
    view using a key stored in FS
    """
    return decrypt_token_rsa(encrypted_message, open(private_key_path).read())
