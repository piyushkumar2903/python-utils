from xml.etree.ElementTree import ElementTree
tree = ElementTree()
root = tree.parse("test.xml")
for node in root.findall('./Items'):
  # print(node)
  for type in list(node):
    if type.find('ProductNo').text == "12345678":
      print(type.find('MD5').text)
      print('found')
    else:
      print("not found")
