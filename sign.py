#!/usr/bin/env python
'''
sign.py
'''
from __future__ import print_function

from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.exceptions import InvalidSignature
import os
import sys

def sign(message, private_key):
    '''
    Signs using an RSA private key using PKCS1v15 Padding and returns the hex
    digest of the signature

    :param str message: The message to sign
    :param str private_key: The private key in PEM format
    :rtype: str
    :return: A hex digest of the signature
    '''

    private_key = serialization.load_pem_private_key(private_key, password=None, backend=default_backend())
    signer = private_key.signer(
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    signer.update(message)
    signature = signer.finalize()
    return signature.encode('hex')


def verify(message, public_key, signature):
    '''
    Verifies a signature of a message. Returns true if the signature matches.

    :param str message: Messare or document that was signed
    :param str public_key: A Public Key in the PEM format
    :param str signature: A Hexadecimal encoded signature
    '''
    public_key = serialization.load_pem_public_key(public_key, backend=default_backend())
    signature = signature.decode('hex')
    verifier = public_key.verifier(
        signature,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    verifier.update(message)
    try:
        verifier.verify()
        return True
    except InvalidSignature:
        return False




if __name__ == '__main__':

    def load(path):
        '''
        Returns the file as a string
        '''
        with open(path, 'r') as f:
            return f.read()

    def main(args):
        document = load(args.document)

        if args.private_key:
            private_key = load(args.private_key)

        if args.public_key:
            public_key = load(args.public_key)

        if args.signature:
            if os.path.exists(args.signature):
                signature = load(args.signature)
            else:
                signature = args.signature
            signature = signature.strip()

        if args.output == '-':
            file_output = sys.stdout
        else:
            file_output = open(args.output, 'w')

        if args.private_key: # Wants to sign
            signature = sign(document, private_key)
            file_output.write(signature)

        elif args.public_key and args.signature:
            verification = verify(document, public_key, signature)
            if verification:
                file_output.write("The signature is valid.\n")
                return 0
            else:
                file_output.write("The signature is invalid.\n")
                return 1

        else:
            print("Either a private key is required to sign or a public key and signature is required to verify", file=sys.stderr)

        if args.output != '-':
            file_output.close()

        return 0
    from argparse import ArgumentParser
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-k', '--private-key', help='Private Key')
    parser.add_argument('-p', '--public-key', help='Path to public key')
    parser.add_argument('-s', '--signature', help='Signature to use')
    parser.add_argument('-o', '--output', default='-', help='Output to use')
    parser.add_argument('document', help='Document or message to be signed')
    args = parser.parse_args()

    sys.exit(main(args))
