from netmiko import ConnectHandler
from my_devices import cisco3, arista1, arista2, srx2
from my_functions import ssh_command
import threading
import time



start = time.time()
net_devices = [cisco3, arista1, arista2, srx2]



for device in net_devices:
   my_thread = threading.Thread(target=ssh_command, args=(device, "show version"))
   my_thread.start()
main_thread= threading.currentThread()

for some_thread in threading.enumerate():
   if some_thread != main_thread:
      print(some_thread)
      some_thread.join()

end = time.time()
print(f"Total execution time:{end-start}")

