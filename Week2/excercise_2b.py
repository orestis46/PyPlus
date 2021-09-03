#! /usr/bin/env python

from netmiko import ConnectHandler
import time

device = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
    "global_delay_factor" : 8,
}

start = time.time()
command = "show lldp neighbors detail"
net_connect = ConnectHandler(**device)
output = net_connect.send_command(command)
end = time.time()
print(output)
print(f'Total execution time:{end-start}')


