import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from nxapi_plumbing import Device
from getpass import getpass
from pprint import pprint
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format = "xml",
    host = "nxos1.lasthop.io",
    username = "pyclass",
    password = getpass(),
    transport = "https",
    port = 8443,
    verify = False
)

cmd = "show interface ethernet1/1"
output = device.show(cmd)
interface = output.find(".//interface")
state = output.find(".//state")
mtu = output.find(".//eth_mtu")
print(f"Interface: {interface.text}; State: {state.text}; MTU: {mtu.text}")

