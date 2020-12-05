
switch : int=0

switch = int(0)


import xml.etree.ElementTree as ET

tree = ET.parse('savegame_1.xml')
root = tree.getroot()



for i in root.findall('world/region'):
    print(i.attrib["coord"])
#change = root.find('world/region/small_tiles/tile')
#ET.SubElement(change, 'tile')

#tree.write('savegame_1.xml')