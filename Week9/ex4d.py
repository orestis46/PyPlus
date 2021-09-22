import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from napalm import get_network_driver
from my_devices import nxos1
from my_functions import napalm_connection, create_checkpoint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

connection = napalm_connection(nxos1)
#create_checkpoint(connection)

Replace_Config = "nxos1.lasthop.io-candidate.cfg"

connection.load_replace_candidate(Replace_Config)
print(f"\n\nThe differences after load_replace_candidate are:\n\n{connection.compare_config()}\n\n")
print(f"Proceeding with discard_config() on {connection.hostname}\n\n")
connection.discard_config()
print(f"\n\nThe differences after discard_config() are:{connection.compare_config()}\n\n")
connection.close()
