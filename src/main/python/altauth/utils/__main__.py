import argparse
import sys
from altauth.utils.utils import (decrypt_token_rsa_using_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decrypt utils.')
    parser.add_argument('command',
                        help='The command  you want to execute',
                        choices=['decrypt_rsa'],)
    parser.add_argument('-p', '--private_key_path',
                        required=False,
                        help='The path to a PEM private key',)
    parser.add_argument('-m', '--encrypted_message',
                        required=False,
                        help='The encrypted message',)
    args = parser.parse_args()
    if args.command == 'decrypt_rsa':
        if not args.private_key_path:
            raise ValueError(args, 'private_key_path is required')
        if args.encrypted_message:
            token = args.encrypted_message
        elif not sys.stdin.isatty():
            token = sys.stdin.read()
        else:
            raise ValueError(args, 'encrypted_message (stdin or argument) is required')
        sys.stdout.write(decrypt_token_rsa_using_file(token, args.private_key_path))
