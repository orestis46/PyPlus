#! /usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime

device = {
    "host": "cisco3.lasthop.io",
    "username": null,
    "password": "null,
    "device_type": "cisco_ios",
    "fast_cli" : "True",
}

start = datetime.now()
commands = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup", "do ping google.com"]
net_connect = ConnectHandler(**device)
output = net_connect.send_config_set(commands)
print(output)
end = datetime.now()
print(f'Total execution time:{end-start}')
net_connect.disconnect()


