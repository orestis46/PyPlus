from lxml import etree

my_xml = etree.parse("show_security_zones.xml")


#print(etree.tostring(my_xml).decode())
out1 = my_xml.find("./zones-security")
print("\n\n")
print("Find tag of the first zones-security element")
print("-" * 20)
print(out1.tag)
