import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label

def area(labeled, label=1):
    return (labeled[labeled == label] / label).sum()

coins = np.load("coins.npy")
areas = {69:0,
         145:0,
         305:0,
         609:0}

labeled = label(coins)
for i in range(1,np.max(labeled)+1):
    a = area(labeled,i)
    for j in areas:
        if j == a:
            areas[j] += 1

summ = 0
nominals = [1,2,5,10]
arrs = []

for i in areas: 
    arrs.append(i)
    
for n in range(0,len(areas)):
    summ += areas[arrs[n]] * nominals[n]
print(summ)