import socket
import urllib.request, urllib.parse, urllib.error

# fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#
# counts = dict()
# for line in fhandle:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# print(counts)


fhand = urllib.request.urlopen('http://coursera.org')
for line in fhand:
    print(line.decode().strip())

# import socketmysock = socket.socket(socket.AF_INET, socket)