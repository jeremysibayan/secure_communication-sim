import json

# open sent packet
with open('packet.json', 'r') as file:
    packet = json.load(file)

# get data to tamper with
encrypted_data = packet['encrypted_data']

# tamper HAHAHAHAHAH
encrypted_data = encrypted_data + "HAHAHAHA, I tampered your data!"

# update packet with the new tampered data
packet['encrypted_data'] = encrypted_data

# write back the tampered packet to file
with open('packet.json', 'w') as file:
    json.dump(packet, file)