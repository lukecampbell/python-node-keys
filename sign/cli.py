#!/usr/bin/env python
'''
sign/cli.py
'''
from __future__ import print_function

from argparse import ArgumentParser
from sign import sign, verify
import sys
import os


def load(path):
    '''
    Returns the file as a string
    '''
    with open(path, 'r') as f:
        return f.read()

def main():
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-k', '--private-key', help='Private Key')
    parser.add_argument('-p', '--public-key', help='Path to public key')
    parser.add_argument('-s', '--signature', help='Signature to use')
    parser.add_argument('-o', '--output', default='-', help='Output to use')
    parser.add_argument('document', help='Document or message to be signed')
    args = parser.parse_args()

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

if __name__ == '__main__':

    sys.exit(main())

