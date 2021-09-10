#! /usr/bin/env python

from netmiko import ConnectHandler


device = {
    "host": "cisco4.lasthop.io",
    "username": null,
    "password": null,
    "device_type": "cisco_nxos",
}

command = "show lldp neighbors"
net_connect = ConnectHandler(**device)
output = net_connect.send_command(command, use_textfsm=True)
print(output[0]['neighbor_interface'])
net_connect.disconnect()


