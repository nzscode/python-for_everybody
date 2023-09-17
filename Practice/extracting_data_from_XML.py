import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "http://py4e-data.dr-chuck.net/comments_1892631.xml"
# url = urllib.parse.urlencode(address)
# uh = urllib.request.urlopen(url, context=ctx)
uh = urllib.request.urlopen(address, context=ctx)


data = uh.read()
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')

count = 0
for item in lst:
    print('Name: ', item.find('name').text)
    print('count: ', item.find('count').text)
    x = item.find('count').text
    count += int(x)

print(count)
