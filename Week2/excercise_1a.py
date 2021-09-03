#! /usr/bin/env python

from netmiko import ConnectHandler

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "fiction",
    "device_type": "cisco_ios"
}

with ConnectHandler(**device) as net_connect:

    cmd = "ping"
    target_ip = "8.8.8.8"

    output = net_connect.send_command_timing(
        cmd, strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        target_ip, strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    print(output)
