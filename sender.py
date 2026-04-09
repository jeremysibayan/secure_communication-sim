from cryptography.fernet import Fernet
from datetime import datetime
import json
import hmac
import hashlib
import secrets

# HMAC Key
hmac_key = b"This is my secret HMAC key"

# create encryption key
key = Fernet.generate_key()

# saves key to a secret.key file
# receiver needs this to decrypt the packet
with open('secret_fernet_key.key', "wb") as key_file:
    key_file.write(key)

# loads key into object for encryption/decryption methods
fernet = Fernet(key)

# dictionary with data to be encrypted and sent
info = {
    'timestamp': datetime.now().isoformat(),
    'my_name': 'John Smith',
    'my_rank': 'Seaman',
    'message': 'High Classified Information...',
    'nonce': secrets.token_hex(8),
}

# converts dict to json string to bytes for encryption via fernet
sent = json.dumps(info).encode()

# encrypt the encoded json bytes of info
encrypted = fernet.encrypt(sent)

# create hmac 
hmac_signature = hmac.new(hmac_key, encrypted, hashlib.sha256).hexdigest()

# package the encrypted string data and hmac signature
packet = {
    "encrypted_data": encrypted.decode(),
    "hmac_signature": hmac_signature
}

# json.dumps =/ json.dump -> dumps converts dict to json string

# writes json object into the file for receiver
with open('packet.json', 'w') as file:
    json.dump(packet, file)

