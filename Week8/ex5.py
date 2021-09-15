from jnpr.junos import Device
from getpass import getpass
from jnpr_devices import srx2
from lxml import etree




a_device = Device(**srx2)
a_device.open()
sh_ver = a_device.rpc.get_software_information()
print(etree.tostring(sh_ver).decode())
sh_int_terse = a_device.rpc.get_interface_information(terse=True)
print(etree.tostring(sh_int_terse).decode())
sh_int_terse_fe007 = a_device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(sh_int_terse_fe007, pretty_print=True).decode())
