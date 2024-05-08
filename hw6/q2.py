dictionary_days = dict() 
fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        day = words[2]
        dictionary_days[day] = dictionary_days.get(day, 0) + 1
print(dictionary_days)