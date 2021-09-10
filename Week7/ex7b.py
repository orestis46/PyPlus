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

cmds= ["show system uptime", "show system resources"]

output = device.show_list(cmds)
for item in output:
   print(etree.tostring(item).decode())


