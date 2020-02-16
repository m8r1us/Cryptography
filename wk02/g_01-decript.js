var chacha20 = require("chacha20");
var crypto = require('crypto');

var keyname="qwerty";
var ciphertext = "e47a2bfe646a";

var args = process.argv;
if (args.length>2) ciphertext=args[2];
if (args.length>3) keyname=args[3];

var key = crypto.createHash('sha256').update(keyname).digest();

var nonce = new Buffer.alloc(8);
nonce.fill(0);

console.log("Ciphertext\t", ciphertext);
console.log("Decipher\t",chacha20.decrypt(key, nonce, new Buffer.from(ciphertext,"hex")).toString());
