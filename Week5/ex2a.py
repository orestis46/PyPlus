from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")


nxos1 = {"intf": "Ethernet1/1", "ip_address": "10.1.100.1", "mask":"/24"}
nxos2 = {"intf": "Ethernet1/1", "ip_address": "10.1.100.2", "mask":"/24"}


for j2 in (nxos1, nxos2):
    template_file = "ex2a_nxos_int.j2"
    template = env.get_template(template_file)
    output = template.render(**j2)
    print(output)

