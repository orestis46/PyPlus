import yaml
import pyeapi
import jinja2
from pprint import pprint
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from getpass import getpass
import ipdb


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")
template_file = "arista.j2"

with open ("arista_full.yml", "r") as f:
    devices = yaml.safe_load(f)


for device, host in devices.items():
    connection = pyeapi.client.connect(transport = host['transport'], host = host['host'], username = host['username'], password = getpass(), port = host['port'])
    j2_data = host['data']
    template = env.get_template(template_file)
    cfg = template.render(**j2_data)
    cfg = cfg.strip()
    cfg = cfg.splitlines()
    print(cfg)
    dev = pyeapi.client.Node(connection)
    output_cfg = dev.config(cfg)
    print(output_cfg)



for device, host in devices.items():
    connection = pyeapi.client.connect(transport = host['transport'], host = host['host'], username = host['username'], password = getpass(), port = host['port'])
    dev = pyeapi.client.Node(connection)
    output_sh = dev.enable("show ip interface brief")
    pprint(output_sh)

