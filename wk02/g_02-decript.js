// RC4
var crypto = require('crypto');

var keyname="napier";
var ciphertext = "8d1cc8bdf6da";
var ciphertext = "911adbb2e6dda57cdaad";
var ciphertext = "8907deba";

var args = process.argv;
if (args.length>2) ciphertext=args[2];
if (args.length>3) keyname=args[3];

var key = crypto.createHash('sha256').update(keyname).digest();

var decipher = crypto.createDecipheriv('rc4', key,'' );
var text = decipher.update(new Buffer.from(ciphertext,"hex"), 'hex','utf8');
console.log("Decipher:\t",text);
