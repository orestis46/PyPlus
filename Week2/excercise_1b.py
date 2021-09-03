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

    output = net_connect.send_command(
        cmd, expect_string = r':', strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "\n", expect_string = r':', strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        target_ip, expect_string = r':', strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "\n", expect_string = r':', strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "\n", expect_string = r':', strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "\n", expect_string = r':', strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "\n", expect_string = r':', strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "\n", expect_string = r':', strip_prompt=False, strip_command=False
    )
    print(output)
