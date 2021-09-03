from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")


VRF_BLUE = {"vrf_name": "blue", "rd_number": "100:1", "ipv4_enabled": True, "ipv6_enabled": True}
VRF_RED = {"vrf_name": "red", "rd_number": "100:2", "ipv4_enabled": True, "ipv6_enabled": True}
VRF_GREEN = {"vrf_name": "green", "rd_number": "100:3", "ipv4_enabled": True, "ipv6_enabled": True}
VRF_ORANGE = {"vrf_name": "orange", "rd_number": "100:4", "ipv4_enabled": True, "ipv6_enabled": True}
VRF_GRAY = {"vrf_name": "gray", "rd_number": "100:5", "ipv4_enabled": True, "ipv6_enabled": True}

VRFs =[VRF_BLUE, VRF_RED, VRF_GREEN, VRF_ORANGE, VRF_GRAY]

vrf_vars = {"vrf_names": VRFs}

template_file = "ex4_vrf.j2"
template = env.get_template(template_file)
output = template.render(vrf_vars)
print(output)
