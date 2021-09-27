from netmiko import ConnectHandler


def ssh_command(device, command):      
   conn = ConnectHandler(**device)
   result = conn.send_command("show version")
   print("="*40)
   print(result)
   print("="*40)
   conn.disconnect()
   return

def ssh_command2(device, command):      
   conn = ConnectHandler(**device)
   result = conn.send_command(command)
   conn.disconnect()
   return(result)
