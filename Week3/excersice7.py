from ciscoconfparse import CiscoConfParse
from pprint import pprint

cisco_obj = CiscoConfParse("xr_bgp_conf.txt")
#neighbors = cisco_obj.find_objects_w_child(parentspec=r"^router bgp", childspec=r"^\s+neighbor")
neighbors = cisco_obj.find_objects_w_parents(parentspec=r"router bgp", childspec=r"neighbor")

bgp_peers = []

for neighbor in neighbors:
    _, neighbor_ip = neighbor.text.split()
    for child in neighbor.children:
        if "remote-as" in child.text:
            _, remote_as = child.text.split()
    bgp_peers.append((neighbor_ip, remote_as))

print()
print("BGP Peers: ")
pprint(bgp_peers)
print()
