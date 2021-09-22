from getpass import getpass
from napalm import get_network_driver
from my_devices import cisco3, arista1


def napalm_connection(device):

   my_device = device
   device_type = my_device.pop("device_type")
   driver = get_network_driver(device_type)
   connect = driver(**my_device)
   connect.open()
   return connect


connections = []
devices = [cisco3, arista1]

for device in devices:
   connect = napalm_connection(device)
   connections.append(connect)
print(connections)
   
