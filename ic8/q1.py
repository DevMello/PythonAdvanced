import urllib.request
import re
input_exp = input('Enter a regular expression: ')
reg_exp = str(input_exp) 
fhand = urllib.request.urlopen('https://raw.githubusercontent.com/ritchieng/python-for-everybody/master/python_data_structures/mbox.txt')
count = 0 

for line in fhand:
    line = line.decode().rstrip()
    if re.findall(reg_exp, line) != []:  
        count += 1

print('The URL had ' + str(count) + ' lines that matched ' + reg_exp)
