import yaml
import pyeapi
from my_funcs import *



arista4 = load_device("arista4.yml")


connection = pyeapi.client.connect(**arista4)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
arp_entries =  output[0]['result']['ipV4Neighbors']
print_output(arp_entries)

