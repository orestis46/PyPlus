#!/usr/bin/env python


arp_list = []
arp_entry = dict()
with open('arp_data.txt') as f:
    for line in f:
        line.strip()
        if 'Hardware Addr' in line:
            continue
        *other, ip_addr, _, mac_addr, _, intf = line.split()
        arp_entry = {"mac_addr": mac_addr, "ip_addr": ip_addr, "intf": intf}
        arp_list.append(arp_entry)
print(arp_list)
