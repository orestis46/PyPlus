from ciscoconfparse import CiscoConfParse
from pprint import pprint

cisco_obj = CiscoConfParse("xr_bgp_conf.txt")
neighbors = cisco_obj.find_objects_w_child(parentspec=r"^router bgp", childspec=r"^\s+neighbor")

peers = neighbors[0].children
_,peer1 = peers[3].text.split()
_,peer2 = peers[4].text.split()

as_1 = peers[3].children
_,peer1_as = as_1[0].text.split()
as_2 = peers[4].children
_,peer2_as = as_2[0].text.split()
bgp_peers = [(peer1, peer1_as), (peer2, peer2_as)]

print(f"BGP Peers:\n{bgp_peers}")
