from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.routes import RouteTable
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2




def  gather_routes(device):

   route_entries = RouteTable(a_device)
   return route_entries.get()



def compare_routes(ini_routes, fin_routes):

   diff_routes = []
   for route in fin_routes.keys():
      if route not in ini_routes.keys():
         diff_routes.append(route)
   return(diff_routes)



a_device = Device(**srx2)
a_device.open()
a_device.timeout = 60
initial_routes = gather_routes(a_device)
#initial_routes (a_device, route_output)
cfg = Config(a_device)
cfg.lock()
cfg.load(path="junos_routes.conf", format="text", merge=True)
cfg.commit()
cfg.unlock()
final_routes = gather_routes(a_device)
routes = compare_routes(initial_routes, final_routes)
print(f"\n\nThe different routes are: {routes}\n\n")
cfg.lock()
cfg.load("delete routing-options static route 203.0.113.5/32", format="set", merge=True)
cfg.load("delete routing-options static route 203.0.113.200/32", format="set", merge=True)
cfg.commit()
cfg.unlock()
