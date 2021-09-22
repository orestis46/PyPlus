from getpass import getpass
from napalm import get_network_driver
from my_devices import cisco3, arista1
from my_functions import napalm_connection
from pprint import pprint



connections = []
devices = [cisco3, arista1]

for device in devices:
   connect = napalm_connection(device)
   connections.append(connect)


for connection in connections:
   connection.load_merge_candidate(filename=f"{connection.hostname}-loopbacks")
   print(f"Before commiting configuration for device {connection.hostname} the differences are:\n\n {connection.compare_config()}")
   connection.discard_config()
   connection.close()

