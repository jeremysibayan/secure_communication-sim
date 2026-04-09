# Secure Communication Simulator

A basic general-purpose project that simulates secure communication system between a sender and receiver using fernet encryption, HMAC authentication, tampering detection, and replay attack protection.

## Files

- 'sender.py'
  Creates a dictionary with info, generates an HMAC signature, and writes the packet.

- 'receiver.py'
  Verifies the integrity of the HMAC, decrypts the packet, and checks for replay attacks referring to already used noncesH.

- 'attacker.py'
  Simulates an makeshift attacker by tampering with packet data.

## Concepts Used

- File-based packet simulation
- Symmetric encryption
- Replay attack protection
- Authentication / Integrity checking

## Sender & Receiver Relationship

- The sender constructs a dictionary containing fields with data to be sent.
-  The dictionary is converted into a JSON string then encoded into bytes to be processed by the encryption.
- The byte-form of the info is encrypted using Fernet key, producing cyphertext.
- An HMAC signature is generated using a shared HMAC key and the ciphertext.
- The sender packages the ciphertext and HMAC signature into one JSON object and writes it a packet file to imitate transmission between a server and client.
- The fernet key is stored in a separate file for the receiver to use.
- The receiver reads the sent JSON packets ciphertext and HMAC signature as strings.
- The JSON string data cannot be interpreted by Fernet, so it is converted back into bytes using .encode().
- The receiver recomputes the HMAC key using the shared HMAC key, and verifies the integrity of the received HMAC.
- If the HMACs do not match, the packet is rejected because it was either tampered with or was not created using the correct HMAC key.
- If the HMACs do match, the fernet key is used to decrypt the data back to its original text in byte form.
- The decrpted bytes are decoded using json.loads(), giving the original dictionary.
- The packet is rejected as a replay attack if the nonce has already been seen. If the nonce is new, it is stored in a list for future checks and is accepted to print to the terminal.

## Failing Simulation Ideas

i) Simulate Tampering:
  - Run sender.py
  - Run attacker.py
  - Run receiver.py

ii) Replay Attack:
  - Run sender.py
  - Run receiver.py
  - Run receiver.py
