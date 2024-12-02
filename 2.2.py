# Ugly but works
import numpy as np
data ='./data/2.1.txt'

total = 0

def check(line):
    line = np.diff(line)
    if (np.min(np.abs(line)) >=1) and (np.max(np.abs(line)) <=3):
            if np.all(line > 0) or np.all(line < 0):
                return True
    else:
         return False
                

for line in open(data, 'r'):
    line = [int(l.replace('\n','')) for l in line.split(' ')]    

    if check(line) == True:
         total += 1
         continue
    
    for i in range(len(line)):    
        res = check(np.delete(line,i))
        if res == True:
            total += 1
            break

print(total)