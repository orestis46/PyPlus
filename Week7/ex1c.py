from lxml import etree

my_xml = etree.parse("show_security_zones.xml")

my_xml = my_xml.getroot()
print("\n\n ----- 1a ----- ")
print(my_xml)
print(type(my_xml))
print("\n\n ----- 1b ----- ")
print(etree.tostring(my_xml).decode())
print("\n\n ----- 1c ----- ")
print(my_xml.tag)
print(len(my_xml))
