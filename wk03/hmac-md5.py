import hashlib
import hmac
import base64

key = b"qwerty123"
message = b"Hello"

print ("HMAC-MD5")
hmacmd5 = hmac.new(key,message,hashlib.md5).digest()
print("\tHex: ", hmacmd5.hex())
print("\tBase64: ", base64.b64encode(hmacmd5).decode())

print ("HMAC-SHA1")
hmacsha1 = hmac.new(key,message,hashlib.sha1).digest()
print("\tHex: ", hmacsha1.hex())
print("\tBase64: ", base64.b64encode(hmacsha1).decode())

print ("HMAC-SHA256")
hmacsha2 = hmac.new(key,message,hashlib.sha256).digest()
print("\tHex: ", hmacsha2.hex())
print("\tBase64: ", base64.b64encode(hmacsha2).decode())

print ("HMAC-SHA512")
hmacsha5 = hmac.new(key,message,hashlib.sha512).digest()
print("\tHex: ", hmacsha5.hex())
print("\tBase64: ", base64.b64encode(hmacsha5).decode())

print ("HMAC-SHA384")
hmacsha3 = hmac.new(key,message,hashlib.sha384).digest()
print("\tHex: ", hmacsha3.hex())
print("\tBase64: ", base64.b64encode(hmacsha3).decode())
