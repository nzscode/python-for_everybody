import xml.etree.ElementTree as ET
from lxml import etree

parser = etree.XMLParser(recover=True,encoding='utf-8')


data = '''
<person>
    <name>Chuck</name>
    <phone type=""intl">
    +1 734 256 2598
    </phone>
    <email hide = "yes"/>
</person>'''

tree = ET.fromstring(data)
xml_file = ET.parse(data, parser=parser)
print('Name:', tree.find('name').text)
