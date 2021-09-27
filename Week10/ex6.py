from netmiko import ConnectHandler
from my_devices import cisco3, arista1, arista2, srx2
from my_functions import ssh_command2
from concurrent.futures import ProcessPoolExecutor, as_completed
import time



start = time.time()
net_devices = [cisco3, arista1, arista2, srx2]
cmds = []
max_procs = 5

with ProcessPoolExecutor(max_procs) as pool:
   for device in net_devices:
      if device['device_type'] != "juniper_junos":
         cmds.append("show ip arp")
      else:
         cmds.append("show arp")
   results_generator = pool.map(ssh_command2, net_devices, cmds)

   for result in results_generator:
      print("-"*40)
      print(result)
      print("-"*40)

end = time.time()
print(f"Total execution time:{end-start}")

