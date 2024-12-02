# %%
import numpy as np

data ='./data/1.2.txt'

rigth, left = [], []

for line in open(data,'r'):
    line = line.split('   ')
    rigth.append(int(line[0]))
    left.append(int(line[1].replace('\n','')))
rigth, left = np.array(rigth), np.array(left)

total =  np.sum([np.sum([left == r]) * r for r in rigth])

print(total)
