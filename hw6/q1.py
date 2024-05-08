count = 0
dictionary_words = dict()

try:
    with open('words.txt') as fhand:
        for line in fhand:
            words = line.split()
            for word in words:
                dictionary_words[word] = None 
except FileNotFoundError:
    print('File cannot be found.')
    exit()

if 'Writing' in dictionary_words:
    print("true")
else:
    print("false")

if 'Hello' in dictionary_words:
    print("true")
else:
    print("false")
