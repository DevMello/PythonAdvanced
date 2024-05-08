import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
characters = 0

for line in fhand:
    characters += len(line.decode())

print(characters)