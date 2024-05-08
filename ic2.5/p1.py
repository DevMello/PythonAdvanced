import re

count = 0  
input_exp = input('Enter a regular expression: ')
reg_exp = str(input_exp)  
fname = 'mbox.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    if re.search(reg_exp, line):
        count += 1

print(fname + ' had ' + str(count) + ' lines that matched ' + reg_exp)