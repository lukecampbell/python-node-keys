"use strict";
/*
 *
 */
var should = require('chai').should(),
    sign   = require('./index');


// For the love of all that is holy do NOT use this private key
var privateKey = `-----BEGIN RSA PRIVATE KEY-----
MIICXwIBAAKBgQFi0sW+ztmZl4oKGQk64vCZ/7xwcwYfqi8cfEgLmksAHCisOQY3
2rI3k6aA6RxeHSCW9JTf5e3tN7T7kviZ/SCCCKJXl6FEq1vO+TfUYa3fAwRh39EY
iwjkE3xSiY3w1bgixzEZGknoTDf7pg6nBk2Dg/4M0KL70UOJZIfnqIOg2wIDAQAB
AoGBAINg24s89+Eg9SGsB3jgUooS4OkaDehnkS4Q7nQtWxvdUUoDi0PfHCHr77jH
l5NZYZnDUeRdNG2jNMX5s0cBLKlEgR/2+xkAUisgWgRmJcbhjTqsWiuEPES1unkP
SrGdW2NHUnALLO/p0AE4hXVqqYlWQa5O87/vvWrrDBtruQjhAkEB0Xwo973UP2mw
krZqob3Y8eBvoLfksU2TEFzbgw68+wMyKyxIr+6kv01Qev2jCMjlW0bioIPQu/hO
7rgY41B0EwJBAMMj2zIzvnQkIV61Luwz05qlAmnAsQzxQgKwPcONA13/j+HG1J5L
BuGslULsPWaVWYZNUuc+WA0yzy9/WbZR6RkCQQGwgesW9n0mRq/YQkKl8l6HsABI
l1WZIPlKtN0J00HpAbk1wDnxro3Jaq8i+FTqLrBdtWmRt6jVXw0IZmpJnFGdAkEA
wfqTu4y6RwNfdKDQ+xXtxC1Bf9R/a2ksADYnv4sejMMtyPb4hj34oj8HxRXHV4Eh
FCMrRRmxN7WJRSLoEBfOiQJBAQlIo9asfe4KjEUW4bneMZ4ma+/QcJAE5CevXzsz
2srNz2XO9T3IiHR6+BkhxQcxR5pBnpECBeY8Ll8FUzBpIi0=
-----END RSA PRIVATE KEY-----`;

var publicKey = `-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQFi0sW+ztmZl4oKGQk64vCZ/7xw
cwYfqi8cfEgLmksAHCisOQY32rI3k6aA6RxeHSCW9JTf5e3tN7T7kviZ/SCCCKJX
l6FEq1vO+TfUYa3fAwRh39EYiwjkE3xSiY3w1bgixzEZGknoTDf7pg6nBk2Dg/4M
0KL70UOJZIfnqIOg2wIDAQAB
-----END PUBLIC KEY-----`;


var validSignature = "011f19afbafa65d63660db61f4b604a07e06e49cc1ca316f1b4eefa3cd5301f8a97edfd2882b0230b884a08d15fde4576632d6d0a1387a37becfd7288e3814bc7e9031de635214b51c6d5c42fe37c00909d9d04cc3712e61c3ac07954214ec018ac79e7fa89ef27258152d341755025a2dda1035aa9f7e415f2f37b65259e13fd7";


describe('#sign', function() {
  var message = "This is a message";
  it('Can produce a valid signature', function() {
    sign.sign(privateKey, message).should.equal(validSignature);
  });
  it('Can verify a valid signature', function() {
    sign.verify(publicKey, message, validSignature).should.equal(true);
  });
});

