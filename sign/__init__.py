#!/usr/bin/env python
'''
sign/__init__.py
'''
from __future__ import print_function

from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.exceptions import InvalidSignature

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




