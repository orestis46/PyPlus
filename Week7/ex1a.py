from lxml import etree

my_xml = etree.parse("show_security_zones.xml")

my_xml = my_xml.getroot()
print(my_xml)
print(type(my_xml))
