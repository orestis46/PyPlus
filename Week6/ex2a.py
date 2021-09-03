import yaml
import pyeapi
from getpass import getpass




with open("arista4.yml") as f:
    devices = yaml.safe_load(f)

arista4 = devices['arista4']
arista4['password'] = getpass()

connection = pyeapi.client.connect(**arista4)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
#print(output)
arp_entries =  output[0]['result']['ipV4Neighbors']
for entry in arp_entries:
    mac = entry['hwAddress']
    ipv4 = entry['address']
    print(f'{mac} --> {ipv4}')

