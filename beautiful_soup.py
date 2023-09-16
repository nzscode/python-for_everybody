import ssl
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"


# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
# lines = soup.find_all('a')
# print(lines[2])
# string_line = str(lines[2])
# r = re.findall('"([a-z].*)"', string_line)
# print(r[0])
#
# url2 = r[0]
# html2 = urlopen(url2, context=ctx).read()
# soup2 = BeautifulSoup(html2, "html.parser")
# lines2 = soup2.find_all('a')
# print(lines2[2])
# string_line2 = str(lines2[2])
# r2 = re.findall('"([a-z].*)"', string_line2)
# print(r2[0])
#
# url3 = r2[0]
# html3 = urlopen(url3, context=ctx).read()
# soup3 = BeautifulSoup(html3, "html.parser")
# lines3 = soup3.find_all('a')
# print(lines3[2])
# string_line3 = str(lines3[2])
# r3 = re.findall('"([a-z].*)"', string_line3)
# print(r3[0])
#
# url4 = r3[0]
# html4 = urlopen(url4, context=ctx).read()
# soup4 = BeautifulSoup(html4, "html.parser")
# lines4 = soup4.find_all('a')
# print(lines4[2])
# string_line4 = str(lines4[2])
# r4 = re.findall('>([A-Za-z]+)', string_line4)
# print(r4[0])

count = 7
position = 18
url = "http://py4e-data.dr-chuck.net/known_by_Riach.html"
final_name = ""
for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    lines = soup.find_all('a')
    # print(lines[2])
    string_line = str(lines[position - 1])
    r = re.findall('"([a-z].*)"', string_line)
    # print(r[0])
    r_name = re.findall('>([A-Za-z]+)', string_line)
    # print(r_name[0])
    final_name = r_name[0]
    url = r[0]

print(final_name)