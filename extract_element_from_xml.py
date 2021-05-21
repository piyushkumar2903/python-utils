from xml.etree.ElementTree import ElementTree
tree = ElementTree()
#parse the XML file - test.xml
root = tree.parse("test.xml")
#iterate over items to find specific product number - 12345678
for node in root.findall('./Items'):
  for type in list(node):
    if type.find('ProductNo').text == "12345678":
      print(type.find('MD5').text)
      print('found')
    else:
      print("not found")
