from netmiko import ConnectHandler
from my_devices import cisco3, arista1, arista2, srx2
from my_functions import ssh_command
import threading
import time



start = time.time()
net_devices = [cisco3, arista1, arista2, srx2]



threads= []

for device in net_devices:
   my_thread = threading.Thread(target=ssh_command, args=(device, "show version"))
   threads.append(my_thread)
   my_thread.start()

for some_thread in threads:
      print(some_thread)
      some_thread.join()

end = time.time()
print(f"Total execution time:{end-start}")

