#!/usr/bin/env node
/*
 * index.js
 */

var fs = require('fs'),
    util = require('util'),
    path = require('path'),
    sign = require('./sign'),
    commander = require('commander'),
    pkg = require(path.join(__dirname, 'package.json'));

commander
    .version(pkg.version)
    .usage('[options] <file>')
    .option('-k, --private-key <private-key>', 'The path to the private key')
    .option('-p, --public-key <public-key>', 'The path to the public key')
    .option('-s, --signature <signature>', 'Path or actual signature to verify')
    .parse(process.argv);

if(commander.args.length < 1) {
  commander.outputHelp();
  process.exit(1);
}
var filePath = commander.args[0];
var message = fs.readFileSync(filePath, 'utf8');

if(commander.privateKey) {
  var privateKey = fs.readFileSync(commander.privateKey, 'utf8');
  var signature = sign.sign(privateKey, message);
  console.log(signature);
  process.exit(0);
} else if(commander.publicKey && commander.signature) {
  var publicKey = fs.readFileSync(commander.publicKey, 'utf8');
  var signature = null;

  if(fs.existsSync(commander.signature)) {
    signature = fs.readFileSync(commander.signature, 'utf8');
  } else {
    signature = commander.signature;
  }
  signature = signature.trim();

  if(sign.verify(publicKey, message, signature)) {
    console.log("The signature is valid.");
    process.exit(0);
  } else {
    console.log("The signature is invalid.");
    process.exit(1);
  }
} else {
  console.error("Either a private key is required to sign or a public key and signature is required to verify");
  process.exit(1);
}


