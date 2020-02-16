// RC4

/**
 * generates random string of characters i.e salt
 * @function
 * @param {number} length - Length of the random string.
 */
var genRandomString = function(length){
    return crypto.randomBytes(Math.ceil(length/2))
            .toString('hex') /** convert to hexadecimal format */
            .slice(0,length);   /** return required number of characters */
};

console.log("-----------------Add Salt to Keyname and hash it (Salt must be stored somewhere)-------------");

var crypto = require('crypto');

var keyname="test";
var plaintext = "testing";
var salt = "hello";
console.log("Plaintext:\t",plaintext);
console.log("keyname:\t",keyname);
console.log("Salt:\t",salt);

// Keyname with salt
keyname = salt + keyname;

console.log("keyname:\t",keyname);
var key = crypto.createHash('sha256').update(keyname).digest();

var cipher = crypto.createCipheriv('rc4', key,'' );
var ciphertext = cipher.update(plaintext, 'utf8', 'hex');
console.log("Ciphertext:\t",ciphertext);


var decipher = crypto.createDecipheriv('rc4', key,'' );
var text = decipher.update( ciphertext, 'hex','utf8');
console.log("Decipher:\t",text);

// ***********************
// or append Salt to ciphertext
// ***********************

console.log("");
console.log("-----------------Append Key To Ciphertext-------------");

var crypto = require('crypto');

var keyname="test";
var plaintext = "testing";
var keylength= 16;
var salt = genRandomString(keylength);
console.log("Plaintext:\t",plaintext);
console.log("keyname:\t",keyname);
console.log("Salt:\t",salt);

// Keyname with salt
keyname = salt + keyname;

console.log("keyname:\t",keyname);
var key = crypto.createHash('sha256').update(keyname).digest();
var cipher = crypto.createCipheriv('rc4', key,'' );
var ciphertext = cipher.update(plaintext, 'utf8', 'hex');
console.log("Ciphertext without salt:\t",ciphertext);

// Add Salt to ciphertext <- Send Ciphertext to client
var ciphertext = salt + ciphertext
console.log("Salt and Ciphertext:\t",ciphertext);

console.log("#> Decipher by reading the salt from the Ciphertext");

// Empty the Key  <- Simulate Client Side
var key="";
var keyname="test";

// Get Salt from Ciphertext
salt = ciphertext.substring(0,keylength);
console.log("Read Salt from ciphertext:\t",salt);

// Prepare Keyname
keyname = salt + keyname;

// Prepare Ciphertext - Cut 8 chars from the beginning
ciphertext = ciphertext.slice(keylength);
console.log("Ciphertext to decrypt:\t",ciphertext);

console.log("keyname:\t",keyname);
var key = crypto.createHash('sha256').update(keyname).digest();
var decipher = crypto.createDecipheriv('rc4', key,'' );
var text = decipher.update( ciphertext, 'hex','utf8');
console.log("Decipher:\t",text);

