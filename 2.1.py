import numpy as np
data ='./data/2.1.txt'

total = 0

for line in open(data, 'r'):
    line = [int(l.replace('\n','')) for l in line.split(' ')]    
    line = np.diff(line)
    
    if (np.min(np.abs(line)) >=1) and (np.max(np.abs(line)) <=3):
        if np.all(line > 0) or np.all(line < 0):
            total += 1

print(total)