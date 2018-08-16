'''
Credits to:
https://gist.github.com/swinton/8409454
http://stackoverflow.com/a/12525165/119849
http://blog.rz.my/2017/11/decrypting-cordova-crypt-file-plugin.html
https://ourcodeworld.com/articles/read/386/how-to-encrypt-protect-the-source-code-of-an-android-cordova-app

Usage with Bash script:
for filename in `find /android_app_location/assets/www/ -type f \( -iname *.htm -o -iname *.html -o -iname *.js -o -iname *.js -o -iname *.css \)` ; do python decrypt-cordova-file.py "secret_key" "iv_value" "$filename" ; done

Standalone usage:
python decrypt-cordova-file.py "secret_key" "iv_value" "$filename"
'''

import sys
import base64
import os
import errno
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = sys.argv[2]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc ))


if not len(sys.argv) == 4:
    print 'Usage: python decrypt-cordova-file.py "secret_key" "iv_value" "$filename"'
    sys.exit(1)

cipher = AESCipher(sys.argv[1])
data= ""
input_file = sys.argv[1]
with open(input_file, 'r') as myfile:
	data=myfile.read().replace('\n', '')
enc_input = data
decrypted = cipher.decrypt(enc_input)
#print decrypted
filename = "decrypted/" + input_file
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(filename, "w") as f:
    f.write(decrypted)
