import json
import urllib.request, urllib.parse, urllib.error

url = "http://py4e-data.dr-chuck.net/comments_1892632.json"
uh = urllib.request.urlopen((url))

data = uh.read().decode()
info = json.loads(data)

print(info["comments"])

count = 0
for person in info["comments"]:
    count += int(person['count'])

print(count)