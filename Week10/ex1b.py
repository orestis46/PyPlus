from netmiko import ConnectHandler
from my_devices import cisco3, arista1, arista2, srx2
import time


def ssh_command(device, command):
   conn = ConnectHandler(**device)
   result = conn.send_command("show version")
   conn.disconnect()
   return(result)

start = time.time()
net_devices = [cisco3, arista1, arista2, srx2]



for device in net_devices:
   output = ssh_command(device, "show version")
   print(output)
end = time.time()
print(f"Total execution time:{end-start}")

