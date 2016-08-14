virtualenv env
source env/bin/activate
pip install -r requirements.txt


# Ted notes
# On my mac since I have a custom build OpenSSL I need to install cryptography module with the following
# LDFLAGS="-L/usr/local/opt/openssl/lib" pip install cryptography --no-use-wheel
# Normally I preceed this with `pip uninstall cryptography`
