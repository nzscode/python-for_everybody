#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# url = serviceurl + urllib.parse.urlencode(parms)
# uh = urllib.request.urlopen(url, context=ctx)
# data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 256 2598
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

dat = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Lucy</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>Travis</name>
        </user>
    </users>
</stuff>        
'''

stuff = ET.fromstring(dat)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get("x"))
