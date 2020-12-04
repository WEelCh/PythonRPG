import xml.etree.ElementTree as ET


tree = ET.parse('Data\\sample_tiles.xml')
root = tree.getroot()

'''
print(ET.tostring(root,encoding='utf8').decode('utf8'))

print(root[0][0].tag)
print(root[0][0].attrib)
obj = root.iter('value')
for i in obj:
    print(i.text)

print(root[0][0].text)
print(root[0][1].text)

root[0][0].text = '3'
tree.write('Data\\format.xml')

#root.findall('./format_data
#/cmd_location/[name="Y-Axis"]'))
'''
"""
for child in root[0]:
    print(child.tag, child.attrib, child[0].tag, child[0].text)

print()

for tile in root.findall('big_tiles'):
    print( tile.find('tile'))
"""

import loader
print(loader.getSmallTile('ger'))