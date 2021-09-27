from netmiko import ConnectHandler
from my_devices import cisco3, arista1, arista2, srx2
from my_functions import ssh_command2
from concurrent.futures import ProcessPoolExecutor, as_completed
import time



start = time.time()
net_devices = [cisco3, arista1, arista2, srx2]

max_procs = 5

with ProcessPoolExecutor(max_procs) as pool:
   process_list = []
   for device in net_devices:
      process  = pool.submit(ssh_command2, device, "show version")
      process_list.append(process)


for proc in as_completed(process_list):
   print("-"*40)
   print(proc.result())
   print("-"*40)

end = time.time()
print(f"Total execution time:{end-start}")

