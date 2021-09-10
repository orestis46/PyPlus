import xmltodict
from pprint import pprint


def load_file(filename):
    xmlfile = open(filename)
    xmldata = xmlfile.read().strip()
    my_xml = xmltodict.parse(xmldata)
    xmlfile.close()
    return my_xml


print("\n\n ----- File 1 ----- ")
file1 = load_file("show_security_zones.xml")
pprint(file1)
print("\n\n ----- File 2 ----- ") 
file2 = load_file("show_security_zones_single_trust.xml")
pprint(file2) 
