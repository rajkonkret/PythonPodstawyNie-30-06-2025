# xml
# xml używa tagów

from xml.dom import minidom

root = minidom.Document()  # <?xml version="1.0" ?>
xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')  # <root></root>
productChild.setAttribute('name', "GFG")  # <product name="GFG"/>
xml.appendChild(productChild)

xml_str = root.toprettyxml(indent='\t')
print(xml_str)

# <?xml version="1.0" ?>
# <root>
# 	<product name="GFG"/>
# </root>
