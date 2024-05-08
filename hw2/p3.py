count  = 0
total = 0.0
fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count +=1
        colpos = line.find(':')
        num = float(line[colpos+1:].strip())
        total += num

if count != 0:
    average = total/count
    print('Average spam confidence:', average)
else:
    print('No lines starting with \"X-DSPAM-Confidence:\" found in the file.')

fhand.close()
