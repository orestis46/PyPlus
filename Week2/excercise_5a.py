#! /usr/bin/env python

from netmiko import ConnectHandler


nxos1 = {
    'device_type': 'cisco_nxos', 
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': 'fiction'
}

nxos2 = {
    'device_type': 'cisco_nxos', 
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': 'fiction'
}

nxos_devices = [nxos1, nxos2]

for device in nxos_devices:
    net_connect = ConnectHandler(**device)
    dev_prompt = net_connect.find_prompt()
    print(dev_prompt)
    output = net_connect.send_config_from_file(config_file='nxos_vlans.txt')
    print(output)
    saved_config = net_connect.save_config()
    print(saved_config)
net_connect.disconnect()

