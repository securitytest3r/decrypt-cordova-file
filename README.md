# Decrypt Files encrypted using Cordova Crypt File Plugin
Python script to decrypt files encrypted using Cordova in Android app

## Where is Secret Key and IV?

1. Decompile APK using Dex2Jar and open JAR file in JD-Gui
2. Secrey Key and IV can be found hardcoded in `com.tkyaki.cordova/DecryptResource.class` file

## Usage

Standalone usage:

```python decrypt-cordova-file.py "secret_key" "iv_value" "$filename"```

Usage with Bash script:

```for filename in `find /android_app_location/assets/www/ -type f \( -iname *.htm -o -iname *.html -o -iname *.js -o -iname *.js -o -iname *.css \)` ; do python decrypt-cordova-file.py "secret_key" "iv_value" "$filename" ; done```

## Credits to:
https://gist.github.com/swinton/8409454

http://stackoverflow.com/a/12525165/119849

http://blog.rz.my/2017/11/decrypting-cordova-crypt-file-plugin.html

https://ourcodeworld.com/articles/read/386/how-to-encrypt-protect-the-source-code-of-an-android-cordova-app
