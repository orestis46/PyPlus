#! /usr/bin/env python

from netmiko import ConnectHandler


device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
}

commands = ["no ip name-server 1.1.1.1", "no ip name-server 1.0.0.1", "no ip domain-lookup"]
net_connect = ConnectHandler(**device)
output = net_connect.send_config_set(commands)
print(output)
net_connect.disconnect()


