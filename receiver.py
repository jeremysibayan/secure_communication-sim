from cryptography.fernet import Fernet
import json
import hmac
import hashlib
import os

# hmac key
hmac_key = b'This is my secret HMAC key'

# reads file from sender for key
with open('secret_fernet_key.key', 'rb') as key_file:
    key = key_file.read()

# create object with received key
fernet = Fernet(key)

# read encrypted packet from sender
with open('packet.json', 'r') as packet_file:
    packet = json.load(packet_file)

# get the encrypted data and hmac signature from loaded packet
encrypted = packet['encrypted_data'].encode()
hmac_signature = packet['hmac_signature']

# create hmac to be compared with the received hmac signature
expected_hmac = hmac.new(hmac_key, encrypted, hashlib.sha256).hexdigest()

# fail if the signatures do not match; there was tampering involved
if not hmac.compare_digest(expected_hmac, hmac_signature):
    print("DATA HAS BEEN TAMPERED WITH")
    exit(1)

# decrypt packet in bytes using fernet key
decrypted = fernet.decrypt(encrypted)

# converts bytes to dict
info = json.loads(decrypted.decode())

# creates a file to store already received nonce numbers after first run
if os.path.exists('received_nonces.json'):
    with open('received_nonces.json', 'r') as nonce_file:
        nonce_num = json.load(nonce_file)
# crates an empty list to store first iteration of nonce numbers for later nonce file
else:
    nonce_num = []

# fail if the nonce number in the received packet is already in the list
if info['nonce'] in nonce_num:
    print("PREVIOUS PACKET REPLAYED")
    exit(1)

# save nonce number to file to prevent replay attacks
nonce_num.append(info['nonce'])

# write the updated list of nonce numbers back
with open('received_nonces.json', 'w') as nonce_file:
    json.dump(nonce_num, nonce_file)

print(info)