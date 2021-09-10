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

cfg_cmds= ["interface loopback146", "description **** nxapi xml_plumbing 1st Loopback ****", "interface loopback147", "description **** nxapi xml_plumbing 2nd Loopback ****"]

output = device.config_list(cfg_cmds)
for item in output:
   print(etree.tostring(item).decode())


