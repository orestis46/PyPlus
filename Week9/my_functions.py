from napalm import get_network_driver


def napalm_connection(device):

   my_device = device
   device_type = my_device.pop("device_type")
   driver = get_network_driver(device_type)
   connect = driver(**my_device)
   connect.open()
   return connect


def create_backup(conn):

   config = conn.get_config("running")["running"]
   filename = conn.hostname +"-running.txt"
   with open(filename, "w") as f:
      f.write(config)

def create_checkpoint(conn):

   filename = conn.hostname +"-checkpoint.txt"
   try:
      backup = conn._get_checkpoint_file()
      with open(filename, "w") as f:
         f.write(backup)
   except Exception:
      print("NX-OS platform supported operation only \n\n")
 
   

