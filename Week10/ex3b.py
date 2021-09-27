from netmiko import ConnectHandler
from my_devices import cisco3, arista1, arista2, srx2
from my_functions import ssh_command2
from concurrent.futures import ThreadPoolExecutor, as_completed
import time



start = time.time()
net_devices = [cisco3, arista1, arista2, srx2]

max_threads = 5

pool = ThreadPoolExecutor(max_threads)
threads_list = []

for device in net_devices:
   thread  = pool.submit(ssh_command2, device, "show version")
   threads_list.append(thread)


for thread in as_completed(threads_list):
   print("-"*40)
   print(thread.result())
   print("-"*40)

end = time.time()
print(f"Total execution time:{end-start}")

