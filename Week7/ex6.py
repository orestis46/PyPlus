import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from nxapi_plumbing import Device
from getpass import getpass
from pprint import pprint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format = "jsonrpc",
    host = "nxos1.lasthop.io",
    username = "pyclass",
    password = getpass(),
    transport = "https",
    port = 8443,
    verify = False
)

cmds = ["show interface ethernet1/1"]
output = device.show_list(cmds)
interface = output[0]['result']['TABLE_interface']['ROW_interface']['interface']
state = output[0]['result']['TABLE_interface']['ROW_interface']['state']
mtu = output[0]['result']['TABLE_interface']['ROW_interface']['eth_mtu']
print(f"Interface: {interface}; State: {state}; MTU: {mtu}")
