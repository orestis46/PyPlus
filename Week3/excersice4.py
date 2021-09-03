import json

with open('arista_data.json') as f:
    arista_data = json.load(f)

arp_entries = arista_data['ipV4Neighbors']
arp_entry = {}
for entry in arp_entries:
    ip_addr = entry['address']
    mac = entry['hwAddress']
    arp_entry[ip_addr] = mac
print(arp_entry)
