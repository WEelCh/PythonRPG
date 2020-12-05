
import xml.etree.ElementTree as ET

tree = ET.parse('savegame_2.xml')
root = tree.getroot()

'''
main = ET.SubElement(root,'test')
sub  = ET.SubElement(main,'subtest')
sub.text = 'Jee'
sub.attrib['Typ'] = '32'
'''

root.clear()

tree.write('savegame_2.xml')

