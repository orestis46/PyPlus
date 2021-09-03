#! /usr/bin/env python

from netmiko import ConnectHandler
#import time
from datetime import datetime

device = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
    "global_delay_factor" : 2,
}

start = datetime.now()
command = "show lldp neighbors detail"
net_connect = ConnectHandler(**device)
output = net_connect.send_command(command)
end = datetime.now()
print(output)
print(f'Total execution time:{end-start}')


