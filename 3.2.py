# %%
import re

data ='./data/3.2.txt'
total = 0
text = ''

for line in open(data,'r'):
    text += line
    
line = ''.join([l.split("don't()")[0] for l in text.split("do()")])
mult_str = re.findall('mul\(\d{1,3},\d{1,3}\)',line)
total += sum([int(m[4:].split(',')[0]) * int(m[4:].split(',')[1].replace(')','')) for m in mult_str])

print(total)