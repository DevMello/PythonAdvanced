string = 'X-DSPAM-Confidence: 0.8475'
col_pos = string.find(':')
num_str = string[col_pos+1:].strip()
num = float(num_str)
print(num)
