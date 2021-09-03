#! /usr/bin/env python

from netmiko import ConnectHandler


device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "fiction",
    "device_type": "cisco_nxos",
}

commands = ["show version", "show lldp neighbors"]
net_connect = ConnectHandler(**device)
for command in commands:
    output = net_connect.send_command(command, use_textfsm=True)
    print(output)
    print(f"\n\n-----------------Type of variable output is: {type(output)}------------------------\n\n")
net_connect.disconnect()


