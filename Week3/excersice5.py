import yaml
from netmiko import ConnectHandler

with open('/home/oiordanidis/.netmiko.yml') as f:
    devices = yaml.safe_load(f)

#print(devices)

cisco3 = devices["cisco3"]

connect = ConnectHandler(**cisco3)
output = connect.find_prompt()
print(output)

