import pyeapi
from getpass import getpass


arista3 = {
    "transport": "https",
    "host": "arista3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "port": 443,
}

connection = pyeapi.client.connect(**arista3)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
#print(output)
arp_entries =  output[0]['result']['ipV4Neighbors']
for entry in arp_entries:
    mac = entry['hwAddress']
    ipv4 = entry['address']
    print(f'{mac} --> {ipv4}')

