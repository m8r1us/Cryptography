#https://stuvel.eu/python-rsa-doc/usage.html
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode
import rsa
import binascii

msg="Pob7AQZZSml618nMwTpx3V74N45x/rTimUQeTl0yHq8F0dsekZgOT385Jls1HUzWCx6ZRFPFMJ1RNYR2Yh7AkQtFLVx9lYDfb/Q+SkinBIBX59ER3/fDhrVKxIN4S6h2QmMSRblh4KdVhyY6cOxu+g48Jh7TkQ2Ig93/nCpAnYQ="
privatekey = "MIICXAIBAAKBgQCwgjkeoyCXm9v6VBnUi5ihQ2knkdxGDL3GXLIUU43/froeqk7q9mtxT4AnPAaDX3f2r4STZYYiqXGsHCUBZcI90dvZf6YiEM5OY2jgsmqBjf2Xkp/8HgN/XDw/wD2+zebYGLLYtd2u3GXx9edqJ8kQcU9LaMH+ficFQyfq9UwTjQIDAQABAoGAD7L1a6Ess+9b6G70gTANWkKJpshVZDGb63mxKRepaJEX8sRJEqLqOYDNsC+pkKO8IsfHreh4vrp9bsZuECrB1OHSjwDB0S/fm3KEWbsaaXDUAu0dQg/JBMXAKzeATreoIYJItYgwzrJ++fuquKabAZumvOnWJyBIs2z103kDz2ECQQDnn3JpHirmgVdf81yBbAJaXBXNIPzOcCth1zwFAs4EvrE35n2HvUQuRhy3ahUKXsKX/bGvWzmC2O6kbLTFEygVAkEAwxXZnPkaAY2vuoUCN5NbLZgegrAtmU+U2woa5A0fx6uXmShqxo1iDxEC71FbNIgHBg5srsUyDj3OsloLmDVjmQJAIy7qLyOA+sCc6BtMavBgLx+bxCwFmsoZHOSX3l79smTRAJ/HY64RREIsLIQ1q/yW7IWBzxQ5WTHgliNZFjKBvQJBAL3t/vCJwRz0Ebs5FaB/8UwhhsrbtXlGdnkOjIGsmV0vHSf6poHqUiay/DV88pvhN11ZG8zHpeUhnaQccJ9ekzkCQDHHG9LYCOqTgsyYms//cW4sv2nuOE1UezTjUFeqOlsgO+WN96b/M5gnv45/Z3xZxzJ4HOCJ/NRwxNOtEUkw+zY="

privatekey = "-----BEGIN RSA PRIVATE KEY-----\n"+privatekey+"\n-----END RSA PRIVATE KEY-----"
#privatekey = b64decode(privatekey)

decryptor= rsa.PrivateKey.load_pkcs1(privatekey)
ciphertext = binascii.a2b_base64(msg)

message = rsa.decrypt(ciphertext, decryptor)
print(message.decode('utf8'))

# b"*`\x13%\xfaL\x9ff\x88\x88\x7f\xbc\xfbzN\xe6z'|{\xad5n\xf2\xe1\xbd9/\xa4x\x1bX\x0c|\xa9\x80\xe0\xb9\x80\xfc\xf9w\xba\xe6y\xd8\x89\x9a\xae`\x07\xaa\x01jcYQD\x12\x87Ar)2"

# b'>\x86\xfb\x01\x06YJiz\xd7\xc9\xcc\xc1:q\xdd^\xf87\x8eq\xfe\xb4\xe2\x99D\x1eN]2\x1e\xaf\x05\xd1\xdb\x1e\x91\x98\x0eO\x7f9&[5\x1dL\xd6\x0b\x1e\x99DS\xc50\x9dQ5\x84vb\x1e\xc0\x91\x0bE-\\}\x95\x80\xdfo\xf4>JH\xa7\x04\x80W\xe7\xd1\x11\xdf\xf7\xc3\x86\xb5J\xc4\x83xK\xa8vBc\x12E\xb9a\xe0\xa7U\x87&:p\xecn\xfa\x0e<&\x1e\xd3\x91\r\x88\x83\xdd\xff\x9c*@\x9d\x84'
