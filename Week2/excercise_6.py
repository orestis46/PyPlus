#! /usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}



net_connect = ConnectHandler(**device)
dev_prompt = net_connect.find_prompt()
print(dev_prompt)
conf_mode = net_connect.config_mode()
print(conf_mode)
exit_mode = net_connect.exit_config_mode()
print(exit_mode)
net_connect.write_channel("disable\n")
out = net_connect.read_channel()
print(out)
net_connect.enable()
dev_prompt = net_connect.find_prompt()
print(dev_prompt)
net_connect.disconnect()
