import xmltodict
from pprint import pprint

xmlfile = open("show_security_zones.xml")
xmldata = xmlfile.read().strip()
my_xml = xmltodict.parse(xmldata)
xmlfile.close()
print("\n\n ----- 2a ----- ")
pprint(my_xml)
print(type(my_xml))
print("\n\n ----- 2b ----- ")
zones = my_xml['zones-information']['zones-security']

print("\n\n ----- Using enumerate(zones) -----")
for i, v in enumerate (zones):
    print(f"Security zone #{i+1}: {v['zones-security-zonename']}")
print("\n\n ----- Using zones.index() -----")
for i in zones:
    print("Security Zone #{0}: {1}".format(zones.index(i)+1, i['zones-security-zonename']))
print("\n\n ----- Using range(len(zones)) -----")
for i in range(len(zones)):
        print("Security Zone #{0}: {1}".format(i+1, zones[i]['zones-security-zonename']))
