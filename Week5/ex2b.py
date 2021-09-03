from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")


nxos1 = {"interface": "Ethernet1/1", "ip_address": "10.1.100.1", "mask":"/24", "local_as" : 22, "remote_peer": "10.1.100.2"}
nxos2 = {"interface": "Ethernet1/1", "ip_address": "10.1.100.2", "mask":"/24", "local_as" : 22, "remote_peer": "10.1.100.1"}


for j2 in (nxos1, nxos2):
    template_file = "ex2b_nxos_int_bgp.j2"
    template = env.get_template(template_file)
    output = template.render(**j2)
    print(output)

