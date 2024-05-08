count = dict()
print("Enter file name: ")
fileName = input(" ")
fh = open(fileName)

for line in fh:
    words = line.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
print(count)