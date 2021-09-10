import xmltodict
from pprint import pprint

xmlfile = open("show_security_zones.xml")
xmldata = xmlfile.read().strip()
my_xml = xmltodict.parse(xmldata)
xmlfile.close()
print("\n\n ----- 2a ----- ")
pprint(my_xml)
print(type(my_xml))

