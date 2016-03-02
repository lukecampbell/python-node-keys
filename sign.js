/*
 * sign.js
 */

var crypto = require('crypto');
const ALGORITHM = 'RSA-SHA256';

module.exports = {
  sign: function(privateKey, message) {
    var signer = crypto.createSign(ALGORITHM);
    signer.update(message);
    return signer.sign(privateKey, 'hex');
  },

  verify: function(publicKey, message, signature) {
    var verifier = crypto.createVerify(ALGORITHM);
    verifier.update(message);
    return verifier.verify(publicKey, signature, 'hex');
  }
}

