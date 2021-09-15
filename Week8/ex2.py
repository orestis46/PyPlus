from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2



def check_connected(device):

   if device.connected:
      print(f"Device: {device} is connected")
   else:
      print(f"Device: {device} is NOT connected")

def  gather_arp_table(device):

   arp_entries = ArpTable(a_device)
   return arp_entries.get()

def  gather_routes(device):

   route_entries = RouteTable(a_device)
   return route_entries.get()



def print_output(device, arp, route):

   output = {}
   output['hostname'] = device.hostname
   output['port'] = device.port
   output['user'] = device.user
   output['arp'] = arp.items()
   output['route'] = route.items()
   pprint(output)

a_device = Device(**srx2)
a_device.open()
check_connected(a_device)
arp_output = gather_arp_table(a_device)
route_output = gather_routes(a_device)
print_output(a_device, arp_output, route_output)

