import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from napalm import get_network_driver
from my_devices import cisco3
from my_functions import napalm_connection, create_checkpoint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

connection = napalm_connection(cisco3)
create_checkpoint(connection)
