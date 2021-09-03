import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
import re

with open("/home/oiordanidis/.netmiko.yml") as f:
    devices = yaml.load(f)

cisco4 = devices['cisco4']
net_connect = ConnectHandler(**cisco4)
output = net_connect.send_command("show run")
net_connect.disconnect()
with open("cisco4_sh_run.txt", "w") as f:
    f.write(output)
cisco_obj = CiscoConfParse("cisco4_sh_run.txt")
intf = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

for int in intf:
    print(f"Interface Line: {int.text}")
    ip_addr = int.re_search_children(r"ip address")[0].text
    print(f"IP Address Line: {ip_addr}")       

