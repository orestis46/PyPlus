import xmltodict
from pprint import pprint


def load_file(filename):
    xmlfile = open(filename)
    xmldata = xmlfile.read().strip()
    my_xml = xmltodict.parse(xmldata)
    xmlfile.close()
    return my_xml

def load_file_list(filename, force_list=None):
    if force_list == None:
        force_list = {}
    xmlfile = open(filename)
    xmldata = xmlfile.read().strip()
    my_xml = xmltodict.parse(xmldata, force_list=force_list)
    xmlfile.close()
    return my_xml


print("\n\n ----- File 1 ----- ")
file1 = load_file("show_security_zones.xml")
pprint(file1)
print(type(file1["zones-information"]["zones-security"]))
print("\n\n ----- File 2 ----- ") 
file2 = load_file("show_security_zones_single_trust.xml")
pprint(file2) 
print(type(file2["zones-information"]["zones-security"]))
print("\n\n ----- File 3 ----- ")
file3 = (load_file_list("show_security_zones_single_trust.xml", force_list={"zones-security": True}))
pprint(file3) 
print(type(file3["zones-information"]["zones-security"]))
