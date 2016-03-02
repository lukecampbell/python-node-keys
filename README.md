# python-node-keys

A proof of concept for signing and verifying documents between node and python


## Installation of Python Packages

```
pip install -r requirements.txt
```

This will install the necessary [`cryptography`](https://cryptography.io/en/latest/) Library.


## Installation of node package dependencies

1. Install nodeJS
2. Install local dependencies
   ```
   npm install
   ```

## Testing

You can test the node project by running

```
npm test
```

## Usage

This project is mostly for a proof of concept and example code for generating
signatures and verifying them in a cross-platform sort of way.

1. Generate a private key
   ```
   openssl genrsa -out test.key 1024
   ```

2. Generate a public key from that private key
   ```
   openssl rsa -in test.key -pubout -out test.pub
   ```

   This generates for us both the private and public key in the PEM format.

3. Create a message document
   ```
   echo "This is a message" > message.txt
   ```

4. Create a signature from node
   ```
   ./index.js -k test.key message.txt > node_signature
   ```

5. Verify the signature from node
   ```
   ./index.js -p test.pub -s node_signature message.txt
   > The signature is valid.
   ```

6. Verify the signature from python
   ```
   ./sign.py -p test.pub -s node_signature message.txt
   > The signature is valid.
   ```

7. Create a signature from python
   ```
   ./sign.py -k test.key message.txt > python_signature
   ```


8. Verify the signature from node
   ```
   ./index.js -p test.pub -s python_signature message.txt
   > The signature is valid.
   ```

9. Verify the signature from python
   ```
   ./sign.py -p test.pub -s python_signature message.txt
   > The signature is valid.
   ```
