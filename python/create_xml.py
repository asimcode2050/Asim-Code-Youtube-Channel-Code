import xml.etree.ElementTree as ET

p = ET.Element('parent')
c = ET.SubElement(p,'child')
comment = ET.Comment('XML Example BY Asim Code')
p.append(comment)
ET.dump(p)
tree = ET.ElementTree(p)
tree.write('outfile.xml')